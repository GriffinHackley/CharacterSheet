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

class FifthEditionCharacter(Character):
    def build(self):
        self.skillList = skill_list_5e
        self.proficiencies = {'skills': [], 'languages':[], 'armor': [], 'weapons':[], 'tools':[], 'savingThrows':[]}       
        self.expertise = {'skills':[], 'tools':[]}

        super().build() 

    def fromCharacter(self, character):
        return super().fromCharacter(character)
    
    def applyBackground(self):
        return

    def getModifiers(self):
        super().getModifiers()
        self.applyBackground()
        
    def calculateSaves(self):
        ret = {}
    
        for ability in Ability:
            statBonus = self.abilityMod[ability.name]
    
            saveName = ability.name + ' Saving Throw'
            bonus, source = self.modList.applyModifier(saveName)

            source['Base'] = statBonus
            
            statBonus += bonus
            if ability.name in self.proficiencies['savingThrows']:
                source['Prof.'] = self.profBonus
                statBonus += self.profBonus

            source = {k: v for k, v in sorted(source.items(), reverse=True, key=lambda item: item[1])}

            ret[ability.name] = {'ability':ability, 'value':statBonus, 'source':source}
    
        return ret

    def calculateAttacks(self):
        ret = {}

        for weapon in self.weapon:
            weaponRet = super().attackInit(weapon)
            
            weaponRet['toHit']['value'] += self.profBonus
            weaponRet['toHit']['source']['Prof.'] = self.profBonus

            if "Melee" in weapon['tags']:
                bonus, source = self.modList.applyModifier('ToHit-Melee')
                weaponRet['toHit']['value'] += bonus
                weaponRet['toHit']['source'].update(source)

            if "Ranged" in weapon['tags']:
                bonus, source = self.modList.applyModifier('ToHit-Ranged')
                weaponRet['toHit']['value'] += bonus
                weaponRet['toHit']['source'].update(source)

                #Parse range increments from weapon properties
                reg = re.compile(r'Range\(([0-9]+)\/([0-9]+)\)')
                if any((match := reg.match(item)) for item in weapon['properties']):
                    closeRange = match.group(1)
                    maxRange   = match.group(2)
                    weaponRet['range'] = closeRange + '/' + maxRange

            damageStat = weapon['damageAbility']
            if 'TWF' in weapon['tags']:
                if 'Main' in weapon['tags']:
                    weaponRet['damageMod']['value'] += self.abilityMod[damageStat]
                    weaponRet['damageMod']['source'][damageStat] = self.abilityMod[damageStat]
                    name = 'Main ' + weapon['name']
                elif 'Off-Hand' in weapon['tags']:
                    name = 'Off-Hand ' + weapon['name']
                else:
                    raise Exception('The TWF tag was on this weapon but neither the Main or Off-Hand tags were found')
            else:
                weaponRet['damageMod']['value'] += self.abilityMod[damageStat]
                weaponRet['damageMod']['source'][damageStat] = self.abilityMod[damageStat]
                name = weapon['name']       
            
            weaponRet['name'] = name

            weaponRet = super().calculateAttack(weaponRet, weapon, 5, 10)

            ret[name] = weaponRet

        return ret
    
    def calculateAC(self):
        bonus, source = self.modList.applyModifier('AC')

        total = 10
        source['Base'] = 10

        total += bonus

        source['Armor'] = self.equipment['armor']['armorBonus']
        total += self.equipment['armor']['armorBonus']

        ability = self.convertEnum(self.equipment['armor']['ability'])
        if self.abilityMod[ability] > self.equipment['armor']['maxAbility']:
            source['Dex*'] = self.equipment['armor']['maxAbility']
            total += self.equipment['armor']['maxAbility']
        else:
            source['Dex'] = self.abilityMod[ability]
            total += self.abilityMod[ability]

        source = {k: v for k, v in sorted(source.items(), reverse=True, key=lambda item: item[1])}

        return {'value':total, 'source':source}
    
    def getProfBonus(self):
        return 2

    def calculateSkills(self):
        ret = {}
        ret["Main"] = {}
        list = skill_list_5e

        for key, value in list.items():
            statBonus = 0

            ability = self.convertEnum(value['ability'])
            statBonus += self.abilityMod[ability]
            bonus, source = self.modList.applyModifier(key)
            source[ability] = statBonus
            statBonus += bonus

            if key in self.proficiencies['skills']:
                if key in self.charClass.expertise['skills']:
                    source['Expertise'] = 2*self.profBonus
                    statBonus += 2*self.profBonus
                else:
                    source['Prof.'] = self.profBonus
                    statBonus += self.profBonus

            ret["Main"][key] = {'ability':ability, 'value':statBonus, 'source':source}
        
        return ret
    
    def applyClass(self):
        super().applyClass()
        self.profBonus = self.getProfBonus()

    def applyBackground(self):
        if self.background == "Spy":
            self.proficiencies['skills'] += ['Acrobatics', 'Sleight of Hand']
            self.proficiencies['tools'] += ['Thieves\' Tools']

        if self.background == "Sage":
            self.proficiencies['skills'] +=  ['Acrobatics', 'History']
            self.proficiencies['languages'] +=  ['Draconic', 'Elvish']

    def getSpells(self):
        ret = self.charClass.getSpells(self.abilityMod, self.profBonus, self.modList)
        return ret

    def getMiscFeatures(self):
        ret = {}

        from ..backgrounds import backgrounds

        ret[self.background['feature']] = backgrounds[self.background['feature']]

        return ret

    def initModifiers(self):
        pass

    def getForms(self, request):
        #TODO: Make this dynamic
        if self.name == "Myriil Taegen":
            combatForm = forms.MyriilCombatForm(request.GET)
            spellForm  = forms.MyriilSpellForm(request.GET)

        if self.name == "Warmund":
            combatForm = forms.WarmundCombatForm(request.GET)
            spellForm  = forms.WarmundSpellForm(request.GET)

        if self.name == "Ezekiel":
            combatForm = forms.EzekielCombatForm(request.GET)
            spellForm  = forms.EzekielSpellForm(request.GET)

        
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
