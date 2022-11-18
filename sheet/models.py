import math
import re
from django.db import models

from sheet.forms import ACTypeForm, MyriilCombatForm, MyriilSpellForm, NailCombatForm, NailSkillForm, NailSpellForm, SacredWeaponForm
from .races import races
from .classes import classes
from .lists import Ability, skill_list_pathfinder, skill_list_5e, save_list_pathfinder, combat_list
from .modifiers import Modifier, ModifierList
from django.template.defaulttags import register

class Character(models.Model):  
    baseStats = models.CharField(max_length=200)

    name = models.CharField(max_length=200)
    race = models.CharField(max_length=200)
    feats = models.JSONField()
    level = models.IntegerField()
    traits = models.JSONField()
    alignment = models.CharField(max_length=200)
    charClass = models.CharField(max_length=200)
    background = models.CharField(max_length=200)
    playerName = models.CharField(max_length=200)

    config = models.JSONField()
 
    armor = models.JSONField()
    weapon = models.JSONField()
    equipment = models.JSONField()
    skillRanks = models.JSONField()

    flavor = models.JSONField()
    
    @classmethod
    def create(cls):
        #Change the first number. Its the character id
        character = cls(4, '', '', '', '', 1, '', '', '', '', '', '', '', '', '', '', '')
        return character
    
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

        self.skillRanks = character.skillRanks
        self.weapon = character.weapon
        self.armor = character.armor
        self.equipment = character.equipment

        self.flavor = character.flavor

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
            self.abilityScores[ability.name] = int(stats[ability.value])
            bonus = self.modList.applyModifier(ability.name)
            self.abilityScores[ability.name] += bonus
            self.abilityMod[ability.name] = math.floor(self.abilityScores[ability.name]/2)-5    
  
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

        # critChance = self.calculateCritChance(ret["Attacks"])

        return ret

    def getConsumables(self):
        ret = {}

        ret.update(self.charClass.getConsumables(self.abilityMod, self.profBonus))
        ret.update(self.race.getConsumables(self.profBonus))

        return ret

    def applyRace(self):
        self.race = races[self.race]
        self.race.appendModifiers(self.modList)
        self.race.addProficiencies(self.proficiencies)

    def applyClass(self):
        self.charClass = classes[self.charClass]
        self.charClass.appendModifiers(self.modList)
        self.charClass.addProficiencies(self.proficiencies)
        self.hitDie = self.charClass.hitDie

        if 'dreadAmbusher' in self.toggles.keys() and self.toggles['dreadAmbusher']:
            self.modList.addModifier(Modifier('1d8', "untyped", 'DamageDie', 'Dread Ambusher'))
        
        if 'elemental' in self.toggles.keys() and self.toggles['elemental']:
            if 'focusWeapon' in self.toggles.keys() and self.toggles['focusWeapon']:
                self.modList.addModifier(Modifier('1d6', "elemental", 'Main-DamageDie', 'Focus Weapon'))
               
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

        if 'shieldOfFaith' in self.toggles.keys() and self.toggles['shieldOfFaith']:
            self.modList.addModifier(Modifier(2, "deflection", 'AC', 'Shield of Faith'))

    def calculateInit(self):
        init = combat_list['Initiative']
        ability = self.convertEnum(init['ability'])
        bonus = self.abilityMod[ability]
        bonus += self.modList.applyModifier('Initiative')

        return bonus
    
    def calculateSpeed(self):
        return 30

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
        attackStat = weapon['toHitAbility']
        toHit  = 0
        toHit += self.abilityMod[attackStat]
        toHit += weapon['bonus']
        toHit += self.modList.applyModifier('ToHit')
        
        #Base Damage
        damageMod = 0
        damageMod += weapon['bonus']
        damageMod += self.modList.applyModifier('Damage')


        #Add weapon die to damage die
        damageDie = weapon['damageDie']
        [number,size] = damageDie.split('d')
        allDie = self.modList.getDieModifier(weapon['tags'])
        if size in allDie.keys():
            allDie[size] = allDie[size] + int(number)
        else:
            allDie[size] = int(number)

        ret = {}
        ret['toHit'] = toHit
        ret['damageMod'] = damageMod
        ret['allDie'] = allDie

        return ret
    
    def calculateAttack(self, attack, weapon, hitPenalty, damageBonus):
        toHit = attack['toHit']
        damageMod = attack['damageMod']
        allDie = attack['allDie']

        #Format Damage Dice
        firstLetter = True
        sortedDieSize = reversed(sorted(list(allDie.keys()))) # Order from highest to smallest die size
        criticalDamage = 0
        averageDamage = 0
        for dieSize in sortedDieSize:
            if firstLetter:
                firstLetter = False
                damageDice = str(allDie[dieSize]) + 'd' + dieSize
            else:
                damageDice = damageDice + '+' + str(allDie[dieSize]) + 'd' + dieSize
            
            #TODO: Implement double dice
            if self.config['critType'] == 'maxDie':
                criticalDamage += allDie[dieSize]*int(dieSize)
            elif self.config['critType'] == 'doubleDice':
                criticalDamage += allDie[dieSize]*((int(dieSize)/2)+.5)
            if self.config['critType'] == 'doubleDice':
                pass
            averageDamage += allDie[dieSize]*((int(dieSize)/2)+.5)
        
        averageDamage += damageMod

        #Power Attack
        powerAttackGraph = self.calculatePowerAttack(toHit, averageDamage, criticalDamage, hitPenalty, damageBonus)
        if self.toggles['powerAttack']:
            toHit = toHit - hitPenalty
            damageMod = damageMod + damageBonus

        #If critical, add extra critical damage
        if self.toggles['critical']:
            if self.config['critType'] == 'maxDie':
                damage = damageDice + f'+{int(damageMod+criticalDamage)} '+ weapon['damageType']
            elif self.config['critType'] == 'doubleDice':
                damage = damageDice +  f'+{damageMod} '+ weapon['damageType']
            elif self.config['critType'] == 'doubleAll':
                #TODO: Implement
                damage = damageDice +  f'+{damageMod} '+ weapon['damageType']
        else:
            damage = damageDice + f'+{damageMod} '+ weapon['damageType']

        ret = {}
        ret['name']             = weapon['name']
        ret['toHit']            = toHit
        ret['damage']           = damage
        ret['damageMod']        = damageMod
        ret['averageDamage']    = averageDamage
        ret['bonusCritDamage']  = criticalDamage
        ret['powerAttackGraph'] = powerAttackGraph

        return ret

    def calculatePowerAttack(self, toHit, damage, critDamage, hitPenalty, damageBonus):
        if "advantage" in self.toggles.keys() and self.toggles["advantage"]:
            if 'Elven Accuracy' in self.feats.values():
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

class PathfinderCharacter(Character):
    def build(self):
        self.skillList = skill_list_pathfinder
        self.proficiencies = {'armor': [], 'weapons':[], 'tools':[], 'languages':[]}       
        self.classSkills = []
        self.profBonus = 0

        super().build()

        self.sacredWeapon = self.getSacredWeapon()
        print(self.sacredWeapon)
    
    def fromCharacter(self, character):
        self.traits = character.traits
        return super().fromCharacter(character)

    def getModifiers(self):
        super().getModifiers()
        self.applyTraits()

    def calculateSaves(self):
        ret = {}

        list = save_list_pathfinder

        for key, value in list.items():
            statBonus = value['value']

            ability = self.convertEnum(value['ability'])
            statBonus += self.abilityMod[ability]
            statBonus += self.modList.applyModifier(key)
            ret[key] = {'ability':ability, 'value':statBonus}
        
        return ret
    
    def calculateAttacks(self):
        ret = {}

        for weapon in self.weapon:
            name = weapon['name']

            critRange = weapon['critRange']

            if self.toggles['focusWeapon']:
                if 'Main' in weapon['tags']:
                    if self.toggles['keen']:
                        critRange = critRange.split('-')
                        range = 20 - int(critRange[0])
                        range = range*2
                        critRange = str(20-range-1) + "-20"

            if 'Kukri' in name:
                weapon['damageDie'] = self.charClass.sacredWeapon['damageDie']
            
            weaponRet = super().attackInit(weapon)

            if self.toggles['confCrit']:
                weaponRet['toHit'] += self.modList.applyModifier('ConfCrit')

            #Power Attack
            hitPenalty  = 1 + math.floor(self.bab/4)
            damageBonus = 2 + 2*math.floor(self.bab/4)

            #Kukri
            if 'Kukri' in name:
                weaponRet['toHit'] += self.modList.applyModifier('ToHit-Kukri')
                weaponRet['damageMod'] += self.modList.applyModifier('Damage-Kukri')

            if 'TWF' in weapon['tags']:
                if 'Main' in weapon['tags']:
                    name = 'Main ' + name
                elif 'Off-Hand' in weapon['tags']:
                    name = 'Off-Hand ' + name
                else:
                    raise Exception('The TWF tag was on this weapon but neither the Main or Off-Hand tags were found')   
            
            #Two-Weapon Fighting
            if self.toggles['twf']:
                damageBonus = math.floor(damageBonus/2)
                if ('Off-Hand' in weapon['tags']) or ('Main' in weapon['tags']):
                    weaponRet['toHit'] -= 2
            else:
                pass

            #If weapon is offhand, add half the ability mod
            #If not add the full ability mod
            damageStat = weapon['damageAbility']
            if 'Off-Hand' in weapon['tags']:
                weaponRet['damageMod'] += int(math.floor(self.abilityMod[damageStat]/2))
            else:
                weaponRet['damageMod'] += self.abilityMod[damageStat]

            weaponRet = super().calculateAttack(weaponRet, weapon, hitPenalty, damageBonus)
          
            weaponRet['name']      = name
            weaponRet['critRange'] = critRange
            weaponRet['critDamage'] = weapon['critDamage']

            ret[name] = weaponRet
        return ret
    
    def getSacredWeapon(self):
        ret = self.charClass.sacredWeapon

        enhanceUsed = 0
        if self.toggles['elemental']:
            enhanceUsed = enhanceUsed + 1
        if self.toggles['keen']:
            enhanceUsed = enhanceUsed+1

        ret['enhanceUsed'] = enhanceUsed

        return ret

    def calculateAC(self):
        total = 10

        if not self.toggles['acType'] == "Touch":
            total += self.armor['armorBonus']

        if not self.toggles['acType'] == "Flat-Footed":
            ability = self.convertEnum(self.armor['ability'])
            if self.abilityMod[ability] > self.armor['maxAbility']:
                total += self.armor['maxAbility']
            else:
                total += self.abilityMod[ability]
        
        if self.toggles['acType'] == "Touch":
            total += self.modList.applyModifierWithFilters('AC',['Natural Armor'])
        elif self.toggles['acType'] == "Flat-Footed":
            total += self.modList.applyModifierWithFilters('AC',['Dodge'])
        else:
            total += self.modList.applyModifier('AC')

        return total

    def calculateSkills(self):
            ret = {}
            list = skill_list_pathfinder

            totalSkillRanks = (self.skillPerLevel+self.abilityMod['Intelligence'])*self.level
            skillRanksUsed  = 0

            if self.toggles['scavenger']:
                self.modList.addModifier(Modifier(2, "racial", 'Perception', 'Scavenger'))
                self.modList.addModifier(Modifier(2, "racial", 'Appraise', 'Scavenger'))

            for key, value in list.items():
                statBonus = value['value']

                ability = self.convertEnum(value['ability'])
                statBonus += self.abilityMod[ability]
                statBonus += self.modList.applyModifier(key)

                if value['acp']:
                    statBonus -= self.armor['armorCheck']

                if key in self.skillRanks:
                    statBonus += int(self.skillRanks[key])
                    skillRanksUsed +=  int(self.skillRanks[key])
                    if key in self.classSkills:
                        statBonus += 3

                if skillRanksUsed > totalSkillRanks:
                    print("Used too many skill ranks")

                ret[key] = {'ability':ability, 'value':statBonus}

            return ret

    def applyClass(self):
        super().applyClass()
        self.classSkills = self.classSkills + self.charClass.classSkills
        self.skillPerLevel = self.charClass.skillPerLevel
        self.bab = self.charClass.bab

    def applyTraits(self):
        #Fate's Favored
        fatesFavored = Modifier(1, "untyped", 'luck', 'Fate\'s Favored')
        self.modList.applyModifierToModifier(fatesFavored)

        # Anatomist
        modifier = Modifier(1, "untyped", 'ConfCrit', 'Anatomist')
        self.modList.addModifier(modifier)

    def getSpells(self):
        ret = self.charClass.getSpells(self.abilityMod, self.modList)
        return ret

    def getMiscFeatures(self):
        ret = {}

        return ret

    def cleanProficiencies(self):
        self.proficiencies['skills'] = self.classSkills
        
        ret = super().cleanProficiencies()

        return ret

    def initModifiers(self):
        naturalArmor = Modifier(0, "Natural Armor", 'AC', 'Iron Skin')
        self.modList.addModifier(naturalArmor)
    


    def getForms(self, request):
        combatForm       = NailCombatForm(request.GET)
        spellForm        = NailSpellForm(request.GET)
        acTypeForm       = ACTypeForm(request.GET)
        skillForm        = NailSkillForm(request.GET)
        sacredWeaponForm = SacredWeaponForm(request.GET)
        
        toggles = {}
        if combatForm.is_valid():
            toggles.update(combatForm.cleaned_data)
        if spellForm.is_valid():
            toggles.update(spellForm.cleaned_data)
        if acTypeForm.is_valid():
            toggles.update(acTypeForm.cleaned_data)
        if skillForm.is_valid():
            toggles.update(skillForm.cleaned_data)
        if sacredWeaponForm.is_valid():
            toggles.update(sacredWeaponForm.cleaned_data)

        self.toggles = toggles

        ret = {}
        ret['acType']        = acTypeForm
        ret['combat']        = combatForm
        ret['spell']         = spellForm
        ret['skill']         = skillForm
        ret['sacredWeapon']  = sacredWeaponForm

        return ret

class FifthEditionCharacter(Character):
    def build(self):
        self.skillList = skill_list_5e
        self.proficiencies = {'skills': [], 'languages':[], 'armor': [], 'weapons':[], 'tools':[], 'savingThrows':[]}       
        self.expertise = {'skills':[], 'tools':[]}

        super().build() 

    def fromCharacter(self, character):
        return super().fromCharacter(character)

    def getModifiers(self):
        super().getModifiers()
        self.applyBackground()
        
    def calculateSaves(self):
        ret = {}
    
        for ability in Ability:
            statBonus = self.abilityMod[ability.name]
    
            saveName = ability.name + ' Saving Throw'
            statBonus += self.modList.applyModifier(saveName)
            if ability.name in self.proficiencies['savingThrows']:
                statBonus += self.profBonus
            ret[ability.name] = {'ability':ability, 'value':statBonus}
    
        return ret

    def calculateAttacks(self):
        ret = {}

        for weapon in self.weapon:
            weaponRet = super().attackInit(weapon)
            
            weaponRet['toHit'] += self.profBonus

            if "Melee" in weapon['tags']:
                weaponRet['toHit'] += self.modList.applyModifier('ToHit-Melee')

            if "Ranged" in weapon['tags']:
                weaponRet['toHit'] += self.modList.applyModifier('ToHit-Ranged')

                #Parse range increments from weapon properties
                reg = re.compile(r'Range\(([0-9]+)\/([0-9]+)\)')
                if any((match := reg.match(item)) for item in weapon['properties']):
                    closeRange = match.group(1)
                    maxRange   = match.group(2)
                    weaponRet['range'] = closeRange + '/' + maxRange

            damageStat = weapon['damageAbility']
            if 'TWF' in weapon['tags']:
                if 'Main' in weapon['tags']:
                    weaponRet['damageMod'] += self.abilityMod[damageStat]
                    name = 'Main ' + weapon['name']
                elif 'Off-Hand' in weapon['tags']:
                    name = 'Off-Hand ' + weapon['name']
                else:
                    raise Exception('The TWF tag was on this weapon but neither the Main or Off-Hand tags were found')
            else:
                weaponRet['damageMod'] += self.abilityMod[damageStat]
                name = weapon['name']       
            
            weaponRet['name'] = name

            weaponRet = super().calculateAttack(weaponRet, weapon, 5, 10)

            ret[name] = weaponRet

        return ret
    
    def calculateAC(self):
        total = 10

        total += self.armor['armorBonus']
        
        ability = self.convertEnum(self.armor['ability'])
        if self.abilityMod[ability] > self.armor['maxAbility']:
            total += self.armor['maxAbility']
        else:
            total += self.abilityMod[ability]
        
        total += self.modList.applyModifier('AC')

        return total
    
    def getProfBonus(self):
        return 2

    def calculateSkills(self):
        ret = {}
        list = skill_list_5e

        for key, value in list.items():
            statBonus = value['value']

            ability = self.convertEnum(value['ability'])
            statBonus += self.abilityMod[ability]
            statBonus += self.modList.applyModifier(key)

            if key in self.proficiencies['skills']:
                statBonus += self.profBonus
                if key in self.charClass.expertise['skills']:
                    statBonus += self.profBonus

            ret[key] = {'ability':ability, 'value':statBonus}
        
        return ret
    
    def applyClass(self):
        super().applyClass()
        self.profBonus = self.getProfBonus()

    def applyBackground(self):
        if self.background == "Spy":
            self.proficiencies['skills'] = self.proficiencies['skills'] + ['Acrobatics', 'Sleight of Hand']
            self.proficiencies['tools'] = self.proficiencies['tools'] + ['Thieves\' Tools']

        if self.background == "Sage":
            self.proficiencies['skills'] = self.proficiencies['skills'] + ['Acrobatics', 'History']
            self.proficiencies['languages'] = self.proficiencies['languages'] + ['Draconic', 'Elvish']

    def getSpells(self):
        ret = self.charClass.getSpells(self.abilityMod, self.profBonus, self.modList)
        return ret

    def getMiscFeatures(self):
        ret = {}

        ret['Wanderer'] = [
{"type": "normal", "text":"""
You have an excellent memory for maps and geography, and you can always recall the general layout of terrain, settlements, and other features around you. In addition, you can find food and fresh water for yourself and up to five other people each day, provided that the land offers berries, small game, water, and so forth.
"""},
]

        return ret

    def initModifiers(self):
        pass

    def getForms(self, request):
        combatForm = MyriilCombatForm(request.GET)
        spellForm  = MyriilSpellForm(request.GET)
        
        toggles = {}
        if combatForm.is_valid():
            toggles.update(combatForm.cleaned_data)
        if spellForm.is_valid():
            toggles.update(spellForm.cleaned_data)

        self.toggles = toggles

        ret = {}
        ret['combat'] = combatForm
        ret['spell'] = spellForm

        return ret