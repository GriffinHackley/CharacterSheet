import math
import re

from django.template.defaulttags import register

import sheet.forms as forms
from sheet.models.Characters import Character

from ..classes import classes
from ..races import races
from ..lists import (Ability, combat_list, save_list_pathfinder, skill_list_5e,
                    skill_list_pathfinder)
from ..modifiers import Modifier, ModifierList

class PathfinderCharacter(Character):
    def build(self):
        self.skillList = skill_list_pathfinder
        self.proficiencies = {'armor': [], 'weapons':[], 'tools':[], 'languages':[], 'skills':[]}       
        self.profBonus = 0
        self.classSkills = []

        super().build()

        self.sacredWeapon = self.getSacredWeapon()
    
    def fromCharacter(self, character):
        self.traits = character.traits
        self.skillRanks = character.skillRanks
        return super().fromCharacter(character)

    def getModifiers(self):
        super().getModifiers()
        self.applyTraits()

    def calculateSaves(self):
        ret = {}

        list = save_list_pathfinder

        for key, value in list.items():
            bonus,source = self.modList.applyModifier(key)
            statBonus = 0
            statBonus += bonus

            ability = self.convertEnum(value['ability'])
            statBonus += self.abilityMod[ability]
            source[ability] = self.abilityMod[ability]

            source = {k: v for k, v in sorted(source.items(), reverse=True, key=lambda item: item[1])}

            ret[key] = {'ability':ability, 'value':statBonus, 'source':source}
        
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
                bonus, source = self.modList.applyModifier('ConfCrit')
                weaponRet['toHit']['value'] += bonus
                weaponRet['toHit']['source'].update(source)

            #Power Attack
            hitPenalty  = 1 + math.floor(self.bab/4)
            damageBonus = 2 + 2*math.floor(self.bab/4)

            #Kukri
            if 'Kukri' in name:
                bonus, source = self.modList.applyModifier('ToHit-Kukri')
                weaponRet['toHit']['value'] += bonus
                weaponRet['toHit']['source'].update(source)

                bonus, source = self.modList.applyModifier('Damage-Kukri')
                weaponRet['damageMod']['value'] += bonus
                weaponRet['damageMod']['source'].update(source)

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
                    weaponRet['toHit']['value'] -= 2
                    weaponRet['toHit']['source']['TWF'] = -2

            #If weapon is offhand, add half the ability mod
            #If not add the full ability mod
            damageStat = weapon['damageAbility']
            if 'Off-Hand' in weapon['tags']:
                bonus = int(math.floor(self.abilityMod[damageStat]/2))
                weaponRet['damageMod']['value'] +=  bonus
                weaponRet['damageMod']['source']['1/2 Str.'] = bonus
            else:
                weaponRet['damageMod']['value'] += self.abilityMod[damageStat]
                weaponRet['damageMod']['source']['Str.'] = self.abilityMod[damageStat]


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

    def calculateCombat(self):
        ret = super().calculateCombat()

        ret["CMD"] = self.calculateCMD()

        return ret

    def calculateAC(self):
        if self.toggles['acType'] == "Touch":
            bonus, source = self.modList.applyModifierWithFilters('AC',['Natural Armor'])
        elif self.toggles['acType'] == "Flat-Footed":
            bonus, source = self.modList.applyModifierWithFilters('AC',['Dodge'])
        else:
            bonus, source = self.modList.applyModifier('AC')

        total = 10
        total += bonus
        source['Base'] = 10

        if not self.toggles['acType'] == "Touch":
            source['Armor'] = self.equipment['armor']['armorBonus']
            total += self.equipment['armor']['armorBonus']

        if not self.toggles['acType'] == "Flat-Footed":
            ability = self.convertEnum(self.equipment['armor']['ability'])
            if self.abilityMod[ability] > self.equipment['armor']['maxAbility']:
                source[ability + "*"] = self.equipment['armor']['maxAbility']
                total += self.equipment['armor']['maxAbility']
            else:
                source[ability] = self.abilityMod[ability]
                total += self.abilityMod[ability]
        
        source = {k: v for k, v in sorted(source.items(), reverse=True, key=lambda item: item[1])}        

        return {'value':total, 'source':source}

    def calculateCMD(self):
        bonus,source = self.modList.applyModifier('CMD')

        source['Base'] = 10
        total = 10
        total += bonus

        source['BAB'] = self.bab
        total += self.bab

        source['Str.'] = self.abilityMod['Strength']
        total += self.abilityMod['Strength']

        source['Dex.'] = self.abilityMod['Dexterity']
        total += self.abilityMod['Dexterity']

        source['Size'] = 0
        total += 0

        source = {k: v for k, v in sorted(source.items(), reverse=True, key=lambda item: item[1])} 

        return {'value':total, 'source':source}

    def calculateSkills(self):
            ret = {}
            ret["Main"] = {}
            ret["Knowledge"] = {}
            list = skill_list_pathfinder

            totalSkillRanks = (self.skillPerLevel+self.abilityMod['Intelligence'])*self.level
            skillRanksUsed  = 0

            if self.toggles['scavenger']:
                self.modList.addModifier(Modifier(2, "racial", 'Perception', 'Scavenger'))
                self.modList.addModifier(Modifier(2, "racial", 'Appraise', 'Scavenger'))

            for key, value in list.items():
                bonus,source = self.modList.applyModifier(key)
                statBonus = 0
                statBonus += bonus

                ability = self.convertEnum(value['ability'])
                statBonus += self.abilityMod[ability]
                source[ability] = self.abilityMod[ability]

                if value['acp']:
                    statBonus -= self.equipment['armor']['armorCheck']
                    source['ACP'] = -self.equipment['armor']['armorCheck']

                skillUsed = False
                if key in self.skillRanks:
                    skillUsed = True
                    statBonus += int(self.skillRanks[key])
                    source['Skill Ranks'] = int(self.skillRanks[key])
                    skillRanksUsed +=  int(self.skillRanks[key])
                    if key in self.classSkills:
                        source['Class Skill'] = 3
                        statBonus += 3

                if skillRanksUsed > totalSkillRanks:
                    raise Exception("You have used {} skill ranks when only {} are available".format(skillRanksUsed, totalSkillRanks))

                source = {k: v for k, v in sorted(source.items(), reverse=True, key=lambda item: item[1])}

                if "Knowledge" in key:
                    if not skillUsed:
                        continue
                    key = key.split(" - ")
                    key = key[1]
                    
                    ret["Knowledge"][key] = {'ability':ability, 'value':statBonus, 'source':source}
                else: 
                    ret["Main"][key] = {'ability':ability, 'value':statBonus, 'source':source}

            return ret

    def applyRace(self):
        super().applyRace()
        self.classSkills = self.classSkills + self.race.skills
    
    def applyBackground(self):
        return

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
        combatForm       = forms.NailCombatForm(request.GET)
        spellForm        = forms.NailSpellForm(request.GET)
        acTypeForm       = forms.ACTypeForm(request.GET)
        skillForm        = forms.NailSkillForm(request.GET)
        sacredWeaponForm = forms.SacredWeaponForm(request.GET)
        
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