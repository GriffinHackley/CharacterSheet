import math
import re
from django.db import models

from sheet.forms import ACTypeForm, MyriilCombatForm, MyriilSpellForm, NailCombatForm, NailSkillForm, NailSpellForm
from .races import races
from .classes import classes
from .lists import Ability, skill_list_pathfinder, skill_list_5e, save_list_pathfinder, combat_list
from .modifiers import Modifier, ModifierList
from django.template.defaulttags import register

class Character(models.Model):  
    config = models.CharField(max_length=200)

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

    gold = models.IntegerField()

    config = models.JSONField()
 
    armor = models.JSONField()
    weapon = models.JSONField()
    equipment = models.JSONField()
    skillRanks = models.JSONField()
    
    # @classmethod
    # def create(cls, edition, baseStats, name, charClass, level, race, background, playerName, alignment, traits, gold, skillRanks, weapon, armor):
    #     character = cls(1, edition, baseStats, name, charClass, level, race, background, playerName, alignment, traits, gold, skillRanks, weapon, armor)
    #     return character
    
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
        self.config = character.config

        self.baseStats = character.baseStats

        self.name = character.name
        self.charClass = character.charClass
        self.level = character.level
        self.race = character.race
        self.background = character.background
        self.feats = character.feats
        self.playerName = character.playerName
        self.alignment = character.alignment
        
        self.gold = character.gold

        self.config = character.config

        self.skillRanks = character.skillRanks
        self.weapon = character.weapon
        self.armor = character.armor
        self.equipment = character.equipment

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

    def getModifiers(self):
        self.initModifiers()
        self.applyRace()
        self.applyClass()
        self.applyFeats()
        self.applySpells()

    def cleanModifiers(self):
        self.modList.cleanModifiers(self.abilityMod)

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

        if "Main Kukri" in ret["Attacks"]:
            ret["PowerAttack"] = ret["Attacks"]["Main Kukri"]

        if "Longbow" in ret["Attacks"]:
            ret["PowerAttack"] = ret["Attacks"]["Longbow"]

        # critChance = self.calculateCritChance(ret["Attacks"])

        return ret

    def applyClass(self):
        self.charClass = classes[self.charClass]
        self.charClass.appendModifiers(self.modList)
        self.hitDie = self.charClass.hitDie

        if 'dreadAmbusher' in self.toggles.keys() and self.toggles['dreadAmbusher']:
            self.modList.addModifier(Modifier('1d8', "untyped", 'DamageDie', 'Dread Ambusher'))
               
    def applyFeats(self):
        ret = {}

        # TODO: ADD source back
        for key, source in self.feats.items():
            if key == "Elven Accuracy":
                self.modList.addModifier(Modifier(1, "untyped", 'Dexterity', 'Elven Accuracy'))
                ret['Elven Accuracy'] = [
{"type": "normal", "text":"""
Whenever you have advantage on an attack roll using Dexterity, Intelligence, Wisdom, or Charisma, you can reroll one of the dice once.
"""}]
            if key == "Sharpshooter":
                ret['Sharpshooter'] = [
{"type": "normal", "text":"""
Attacking at long range doesn't impose disadvantage on your ranged weapon attack rolls.

Your ranged weapon attacks ignore half and three-quarters cover.

Before you make an attack with a ranged weapon that you are proficient with, you can choose to take a -5 penalty to the attack roll. If that attack hits, you add +10 to the attack's damage.
"""}]
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
        ret['Items'] = {}

        from pprint import pprint

        # pprint(ret)

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
        self.proficiencies = {'armor': [], 'weapons':[], 'tools':[]}       
        self.classSkills = []
        
        super().build()
    
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

            if 'Kukri' in name:
                weapon['damageDie'] = self.charClass.sacredWeapon
            
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
            weaponRet['critRange'] = weapon['critRange']
            weaponRet['critDamage'] = weapon['critDamage']

            ret[name] = weaponRet
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
                self.modList.addModifier(Modifier(2,"racial", 'Perception', 'Scavenger'))

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

    def applyRace(self):
        self.race = races[self.race]
        self.race.appendModifiers(self.modList)
        self.classSkills = self.classSkills + self.race.classSkills

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

    def calculateCombat(self):
        ret = super().calculateCombat()
        
        ret["Consumables"] = self.charClass.getConsumables(self.abilityMod)

        return ret

    def getSpells(self):
        ret = self.charClass.getSpells(self.abilityMod, self.modList)
        return ret

    def initModifiers(self):
        naturalArmor = Modifier(0, "Natural Armor", 'AC', 'Iron Skin')
        self.modList.addModifier(naturalArmor)

    def getForms(self, request):
        combatForm = NailCombatForm(request.GET)
        spellForm  = NailSpellForm(request.GET)
        acTypeForm = ACTypeForm(request.GET)
        skillForm  = NailSkillForm(request.GET)
        
        toggles = {}
        if combatForm.is_valid():
            toggles.update(combatForm.cleaned_data)
        if spellForm.is_valid():
            toggles.update(spellForm.cleaned_data)
        if acTypeForm.is_valid():
            toggles.update(acTypeForm.cleaned_data)
        if skillForm.is_valid():
            toggles.update(skillForm.cleaned_data)

        self.toggles = toggles

        ret = {}
        ret['acType'] = acTypeForm
        ret['combat'] = combatForm
        ret['spell']  = spellForm
        ret['skill']  = skillForm

        return ret

class FifthEditionCharacter(Character):
    def build(self):
        self.skillList = skill_list_5e
        self.proficiencies = {'skills': [], 'armor': [], 'weapons':[], 'tools':[], 'saving throws':[]}       
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
            if ability.name in self.proficiencies['saving throws']:
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
    
    def applyRace(self):
        self.race = races[self.race]
        self.race.appendModifiers(self.modList)
        self.race.addProficiencies(self.proficiencies)
    
    def applyClass(self):
        super().applyClass()
        currentClass = self.charClass
        currentClass.addProficiencies(self.proficiencies)
        self.profBonus = self.getProfBonus()

    def applyBackground(self):
        self.proficiencies['skills'] = self.proficiencies['skills'] + ['Acrobatics', 'Sleight of Hand']
        self.proficiencies['tools'] = self.proficiencies['tools'] + ['Thieves\' Tools']

    def calculateCombat(self):
        ret = super().calculateCombat()

        ret["Consumables"] = self.charClass.getConsumables(self.abilityMod, self.profBonus)

        return ret

    def getSpells(self):
        ret = self.charClass.getSpells(self.abilityMod, self.profBonus, self.modList)
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