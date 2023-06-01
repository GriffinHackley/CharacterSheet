import math

from django.template.defaulttags import register

from ..classes import classes
from ..races import races
from ..lists import (Ability, combat_list, save_list_pathfinder, skill_list_5e,
                    skill_list_pathfinder)
from ..modifiers import Modifier, ModifierList

class Character():  
    def create(cls):
        pass
    
    @register.filter
    def get_item(dictionary, key):
        return dictionary.get(key)

    @property
    def attribute(self):
        return self._attribute

    @attribute.setter
    def attribute(self, value):
        self._attribute = value

    @attribute.deleter
    def attribute(self):
        del self._attribute

    def __str__(self):
        return self.name

    def fromCharacter(self, character):
        self.baseStats = character.baseStats

        self.name = character.name
        self.charClass = character.charClass
        self.level = character.level
        self.race = character.race
        self.background = character.background
        self.feats = character.feats
        self.playerName = character.playerName
        self.alignment = character.alignment

        self.config = character.config

        self.weapon = character.weapon
        self.equipment = character.equipment

        self.flavor = character.flavor

        self.accentColor = character.accentColor

        self.fullChar = character

        return self

    def build(self):
        self.modList = ModifierList()
        self.getModifiers()
        self.calculateStats()
        self.cleanModifiers()
        self.saves = self.calculateSaves()
        self.skills = self.calculateSkills()
        self.combat = self.calculateCombat()
        self.equipment = self.getEquipment()
        self.spells = self.getSpells()
        self.features = self.getFeatures()
        self.proficiencies = self.cleanProficiencies()

    def getModifiers(self):
        self.initModifiers()
        self.applyRace()
        self.applyBackground()
        self.applyClass()
        self.applyFeats()
        self.applySpells()

    def cleanModifiers(self):
        self.modList.cleanModifiers(self.abilityMod, self.profBonus)

    def calculateStats(self):
        stats = self.decodeStats()

        self.abilityScores = {}
        self.abilityMod = {}

        for ability in Ability:
            self.abilityScores[ability.name] = {}
            base = int(stats[ability.value])
            bonus,source = self.modList.applyModifier(ability.name)

            # Add base score and sort sources from highest to lowest
            source['Base'] = base
            source = {k: v for k, v in sorted(source.items(), reverse=True, key=lambda item: item[1])}

            self.abilityScores[ability.name]['value'] = base+bonus
            self.abilityScores[ability.name]['source'] = source
            self.abilityMod[ability.name] = math.floor(self.abilityScores[ability.name]['value']/2)-5  
  
    def calculateCombat(self):
        ret = {}

        ret["Initiative"]  = self.calculateInit()
        ret["Speed"]       = self.calculateSpeed()
        ret["HP"]          = self.calculateHP()
        ret["AC"]          = self.calculateAC()
        ret["Attacks"]     = self.calculateAttacks()
        ret["Consumables"] = self.getConsumables()

        if "Main Kukri" in ret["Attacks"]:
            ret["PowerAttack"] = ret["Attacks"]["Main Kukri"]

        if "Longbow" in ret["Attacks"]:
            ret["PowerAttack"] = ret["Attacks"]["Longbow"]

        if "Rapier" in ret["Attacks"]:
            ret["PowerAttack"] = ret["Attacks"]["Rapier"]

        # critChance = self.calculateCritChance(ret["Attacks"])

        return ret

    def getConsumables(self):
        ret = {}

        ret.update(self.charClass.getConsumables(self.abilityMod, self.profBonus))
        ret.update(self.race.getConsumables(self.profBonus))

        return ret

    def applyRace(self):
        allRaces = races.allRaces()
        raceModule = allRaces[self.race['name']]
        self.race = getattr(raceModule, self.race['name'].replace("-", "").replace(" ", ""))(self.race['options'])
        self.race.appendModifiers(self.modList)
        self.race.addProficiencies(self.proficiencies)
    
    def applyClass(self):
        allClasses = classes.allClasses()
        classModule = allClasses[self.charClass['name'].lower()]
        self.charClass = getattr(classModule, self.charClass['name'])(self.level, self.charClass['options'])
        self.charClass.appendModifiers(self.modList)
        self.charClass.addProficiencies(self.proficiencies)
        self.hitDie = self.charClass.hitDie

        if 'dreadAmbusher' in self.toggles.keys() and self.toggles['dreadAmbusher']:
            self.modList.addModifier(Modifier('1d8', "untyped", 'DamageDie', 'Dread Ambusher'))
        
        if 'elemental' in self.toggles.keys() and self.toggles['elemental']:
            if 'focusWeapon' in self.toggles.keys() and self.toggles['focusWeapon']:
                self.modList.addModifier(Modifier('1d6', "elemental", 'Main-DamageDie', 'Focus Weapon'))
        
        if 'bladesong' in self.toggles.keys() and self.toggles['bladesong']:
            self.modList.addModifier(Modifier('Intelligence', "untyped", 'AC', 'Bladesong'))
            self.modList.addModifier(Modifier(10, "untyped", 'Speed', 'Bladesong'))
            pass

    def applyFeats(self):
        ret = {}

        # TODO: ADD source back
        for key, source in self.feats.items():
            if key == "Elven Accuracy":
                self.modList.addModifier(Modifier(1, "untyped", 'Dexterity', 'Elven Accuracy'))
                ret['Elven Accuracy'] = [
                    {"type": "normal", "text":"Whenever you have advantage on an attack roll using Dexterity, Intelligence, Wisdom, or Charisma, you can reroll one of the dice once."}]

            if key == "Sharpshooter":
                ret['Sharpshooter'] = [
                    {"type": "normal", "text":"""
                    Attacking at long range doesn't impose disadvantage on your ranged weapon attack rolls.

                    Your ranged weapon attacks ignore half and three-quarters cover.

                    Before you make an attack with a ranged weapon that you are proficient with, you can choose to take a -5 penalty to the attack roll. If that attack hits, you add +10 to the attack's damage.
                    """}]

            if key == "Two-Weapon Fighting":
                ret['Two-Weapon Fighting'] = [
                    {"type": "heading", "text":"Benefit:"},
                    {"type": "normal", "text":"Your penalties on attack rolls for fighting with two weapons are reduced. The penalty for your primary hand lessens by 2 and the one for your off hand lessens by 6."},

                    {"type": "heading", "text":"Normal:"},
                    {"type": "normal", "text":"If you wield a second weapon in your off hand, you can get one extra attack per round with that weapon. When fighting in this way you suffer a –6 penalty with your regular attack or attacks with your primary hand and a –10 penalty to the attack with your off hand. If your off-hand weapon is light, the penalties are reduced by 2 each. An unarmed strike is always considered light."},
                ]

            if key == "Butterfly Sting":
                ret['Butterfly Sting'] = [
                    {"type": "normal", "text":"When you confirm a critical hit against a creature, you can choose to forgo the effect of the critical hit and grant a critical hit to the next ally who hits the creature with a melee attack before the start of your next turn. Your attack only deals normal damage, and the next ally automatically confirms the hit as a critical."},]

            if key == "Combat Reflexes":
                ret['Combat Reflexes'] = [
                    {"type": "heading", "text":"Benefit:"},
                    {"type": "normal", "text":"You may make a number of additional attacks of opportunity per round equal to your Dexterity bonus. With this feat, you may also make attacks of opportunity while flat-footed."},

                    {"type": "heading", "text":"Normal"},
                    {"type": "normal", "text":"A character without this feat can make only one attack of opportunity per round and can’t make attacks of opportunity while flat-footed."},
                ]

        self.feats = ret

    def applySpells(self):
        if 'absorbElements' in self.toggles.keys() and self.toggles['absorbElements']:
            self.modList.addModifier(Modifier('1d6', "elemental", 'Melee-DamageDie', 'Absorb Elements'))

        if 'boomingBlade' in self.toggles.keys() and self.toggles['boomingBlade']:
            self.modList.addModifier(Modifier('0d8', "untyped", 'DamageDie', 'Booming Blade'))

        if 'catsGrace' in self.toggles.keys() and self.toggles['catsGrace']:
            self.modList.addModifier(Modifier(4, "enhancement", 'Dexterity', 'Cats Grace'))

        if 'divineFavor' in self.toggles.keys() and self.toggles['divineFavor']:
            self.modList.addModifier(Modifier(1, "luck", 'ToHit', 'Divine Favor'))
            self.modList.addModifier(Modifier(1, "luck", 'Damage', 'Divine Favor'))
        
        if 'favoredFoe' in self.toggles.keys() and self.toggles['favoredFoe']:
            self.modList.addModifier(Modifier('1d4', "untyped", 'DamageDie', 'Favored Foe'))
        
        if 'huntersMark' in self.toggles.keys() and self.toggles['huntersMark']:
            self.modList.addModifier(Modifier('1d6', "untyped", 'DamageDie', 'Hunters Mark'))
        
        if 'ironSkin' in self.toggles.keys() and self.toggles['ironSkin']:
            self.modList.applyModifierToModifier(Modifier(4, "enhancement", 'Natural Armor', 'Iron Skin'))

        if 'shield' in self.toggles.keys() and self.toggles['shield']:
            self.modList.addModifier(Modifier(5, "untyped", 'AC', 'Shield'))

        if 'shieldOfFaith' in self.toggles.keys() and self.toggles['shieldOfFaith']:
            self.modList.addModifier(Modifier(2, "deflection", 'AC', 'Shield of Faith'))

    def calculateInit(self):
        modifier,source = self.modList.applyModifier('Initiative')

        init = combat_list['Initiative']
        ability = self.convertEnum(init['ability'])
        bonus = self.abilityMod[ability]
        source[ability] = self.abilityMod[ability]

        bonus += modifier

        source = {k: v for k, v in sorted(source.items(), reverse=True, key=lambda item: item[1])}

        return {'value':bonus, 'source':source}
    
    def calculateSpeed(self):
        bonus, source = self.modList.applyModifier('Speed')
        
        source['Base'] = self.race.speed
        speed = self.race.speed

        speed += bonus

        source = {k: v for k, v in sorted(source.items(), reverse=True, key=lambda item: item[1])}

        return {'value':speed, 'source':source}

    def calculateHP(self):
        #Level one max die
        die = int(self.hitDie)
        
        #Average roll of hitdie
        hpPerLevel = (die/2)+1
        die += (self.level-1)*hpPerLevel

        #Add Constitution
        hpPerLevel = self.abilityMod['Constitution']
        die += self.level*hpPerLevel

        return int(die)
    
    def calculateCritChance(self, attacks):
        # Nail
        # main = self.critChance(attacks['Main Kukri'])
        # off = self.critChance(attacks['Off-Hand Kukri'])

        # none = (1-main)*(1-off)
        # one = 1-none
        # two = main*off

        # return (none*100, one*100, two*100)

        #Myriil
        #Chance of not critting on an attack
        if 'advantage' in self.toggles and self.toggles['advantage']:
            baseChance = pow(.95,3)
        else:
            baseChance = .05

        if 'dreadAmbusher' in self.toggles and self.toggles['dreadAmbusher']:
            #chance of not critting on either attack
            overall = pow(baseChance,2)
        else:
            #chance of not critting on only first attack
            overall = baseChance
        
        return {'one': 1-baseChance, 'multiple': 1-overall}

    def critChance(self, attack):
        critRange = attack['critRange']
        critRange = int(critRange.split("-")[0])
        critChance = (21-critRange)/20
        return critChance

    def attackInit(self, weapon):
        #Base to Hit
        bonus, toHitSource = self.modList.applyModifier('ToHit')

        toHit = 0
        toHit += bonus
        attackStat = weapon['toHitAbility']
        toHit += self.abilityMod[attackStat]
        toHitSource[attackStat] = self.abilityMod[attackStat]
        
        #Base Damage
        damageMod = 0
        damageMod += weapon['bonus']
        bonus, damageSource = self.modList.applyModifier('Damage')
        damageMod += bonus

        if weapon['bonus'] > 0:
            toHit += weapon['bonus']
            toHitSource['Enchant'] = weapon['bonus']
            damageSource['Enchant'] = weapon['bonus']

        #Add weapon die to damage die
        allDie, dieSource = self.modList.getDieModifier(weapon['tags'])

        dieSource["Weapon Die"] = weapon['damageDie']
        damageDie = weapon['damageDie']
        [number,size] = damageDie.split('d')
        if size in allDie.keys():
            allDie[size] = allDie[size] + int(number)
        else:
            allDie[size] = int(number)

        ret = {}
        ret['toHit'] = {'value':toHit, 'source':toHitSource}
        ret['damageMod'] = {'value':damageMod, 'source':damageSource}
        ret['allDie'] = {'value':allDie, 'source':dieSource}

        return ret
    
    def calculateAttack(self, attack, weapon, hitPenalty, damageBonus):
        toHit = attack['toHit']['value']
        toHitSource = attack['toHit']['source']

        damageMod = attack['damageMod']['value']
        damageSource = attack['damageMod']['source']

        allDie = attack['allDie']
        dieSource = attack['allDie']['source']

        #Format Damage Dice
        firstLetter = True
        sortedDieSize = reversed(sorted(list(allDie['value'].keys()))) # Order from highest to smallest die size
        criticalDamage = 0
        averageDamage = 0
        for dieSize in sortedDieSize:
            damageDie = allDie['value'][dieSize]

            if self.toggles['critical']:
                if self.config['critType'] == 'doubleDice' or self.config['critType'] == 'doubleAll':
                    damageDie = damageDie*2
            
            if firstLetter:
                firstLetter = False
                damageDice = str(damageDie) + 'd' + dieSize
            else:
                damageDice = damageDice + '+' + str(damageDie) + 'd' + dieSize
            
            #Calculate critical damage
            if self.config['critType'] == 'maxDie':
                criticalDamage += allDie['value'][dieSize]*int(dieSize)
            elif self.config['critType'] == 'doubleDice':
                criticalDamage += allDie['value'][dieSize]*((int(dieSize)/2)+.5)
            elif self.config['critType'] == 'doubleDice':
                pass
            averageDamage += allDie['value'][dieSize]*((int(dieSize)/2)+.5)
        
        averageDamage += damageMod

        #Power Attack
        powerAttackGraph = self.calculatePowerAttack(toHit, averageDamage, criticalDamage, hitPenalty, damageBonus)
        if 'powerAttack' in self.toggles and self.toggles['powerAttack']:
            toHit = toHit - hitPenalty
            toHitSource["Power Attk."] = -hitPenalty

            damageMod = damageMod + damageBonus
            damageSource["Power Attk."] = damageBonus

        #If critical, add extra critical damage
        if self.toggles['critical']:
            if self.config['critType'] == 'maxDie':
                damage = damageDice + f'+{int(damageMod+criticalDamage)} '+ weapon['damageType']
            elif self.config['critType'] == 'doubleAll':
                damage = damageDice + f'+{2*damageMod} '+ weapon['damageType']
            else:
                damage = damageDice + f'+{damageMod} '+ weapon['damageType']
        else:
            damage = damageDice + f'+{damageMod} '+ weapon['damageType']

        toHitSource = {k: v for k, v in sorted(toHitSource.items(), reverse=True, key=lambda item: item[1])}
        damageSource = {k: v for k, v in sorted(damageSource.items(), reverse=True, key=lambda item: item[1])}
        dieSource = dict(reversed(sorted(dieSource.items(), key=lambda x:x[1])))

        dieSource.update(damageSource)

        ret = {}
        ret['name']             = weapon['name']
        ret['toHit']            = {'value':toHit, 'source':toHitSource}
        ret['damage']           = {'value':damage, 'source':dieSource}
        ret['damageMod']        = damageMod
        ret['averageDamage']    = averageDamage
        ret['bonusCritDamage']  = criticalDamage
        ret['powerAttackGraph'] = powerAttackGraph

        return ret

    def calculatePowerAttack(self, toHit, damage, critDamage, hitPenalty, damageBonus):
        if "advantage" in self.toggles.keys() and self.toggles["advantage"]:
            if 'Elven Accuracy' in self.feats.keys():
                timesRolling = 3
            else:
                timesRolling = 2
        else :
            timesRolling = 1

        critChance = 1-pow(.95, timesRolling)

        ret = {'AC':[], 'normal':[], 'powerAttack':[]}
        for targetAC in range(toHit+1, toHit+22):
            chancePerRoll = 0.05*(targetAC-toHit-1)
            hitChance = 1 - pow(chancePerRoll, timesRolling)

            powerchancePerRoll = 0.05*(targetAC-toHit-1+hitPenalty)
            powerHitChance = 1 - pow(powerchancePerRoll, timesRolling)

            avgCritDamage = critChance*critDamage

            if hitChance >= 1:
                hitChance = 1
            if powerHitChance >= 1:
                powerHitChance = 1

            if 1-chancePerRoll <= 0:
                normalDamage = (.05*damage) + avgCritDamage
            else:
                normalDamage = (hitChance*damage) + avgCritDamage
            
            if 1-powerchancePerRoll <= 0:
                powerDamage  = (.05*damage) + avgCritDamage + (critChance*damageBonus)
            else:
                powerDamage  = ((powerHitChance*(damage+damageBonus))) + avgCritDamage

            ret['AC'].append(targetAC)
            ret['normal'].append( round(normalDamage, 3) )
            ret['powerAttack'].append( round(powerDamage, 3) )

            if normalDamage > powerDamage:
                ret['threshold'] = targetAC-1
        
        return ret

    def getEquipment(self):
        for item in self.equipment:
            self.equipment[item]['displayName'] = "| " + self.equipment[item]['name']
        
        return self.equipment

    def getFeatures(self):
        ret = {}

        ret['Class'] = self.charClass.getClassFeatures()
        ret['Feats'] = self.getFeats()
        ret['Race']  = self.race.getFeatures()
        ret['Misc.'] = self.getMiscFeatures()

        return ret

    def cleanProficiencies(self):
        ret = {}
        for item, value in self.proficiencies.items():
            if item == "armor" or item=="weapons":
                ret[item] = value
            else:
                ret[item] = sorted(value)

        return ret

    def getFeats(self):
        return self.feats

    def decodeStats(self):
        stats = self.baseStats
        return stats.split(",")

    def convertEnum(self, enum):
        index = Ability[enum].value
        return Ability(index).name
    
    def addWeapon(self, weapon):
        self.weapon.append(weapon)