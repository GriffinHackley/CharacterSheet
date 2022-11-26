from .classes import Class
from ..modifiers import Modifier, ModifierList

class Ranger(Class):
    proficiencies = {'skills': ['Insight', 'Stealth', 'Survival'], 'languages':['Draconic', 'Sylvan'], 'armor': ['Light', 'Medium'], 'weapons':['Simple', 'Martial'], 'tools':[], 'savingThrows':['Strength', 'Dexterity']}
    expertise = {'skills': ['Stealth']}

    def __init__(self, level, options):
        self.options = options
        super().__init__(level, name="Ranger", hitDie='10', edition="5e")

    def appendModifiers(self, modList: ModifierList):
        super().appendModifiers(modList)

        modList.addModifier(Modifier(2,"untyped", 'ToHit-Ranged', 'Archery Fighting Style'))
        modList.addModifier(Modifier('Wisdom',"untyped", 'Initiative', 'Dread Ambusher'))

    def getConsumables(self, stats, proficiencyBonus):
        huntersMark = stats['Wisdom']
        favoredFoe = proficiencyBonus
        return {'Favored Foe': favoredFoe, 'Hunters Mark': huntersMark}
    
    def getSpells(self, stats, profBonus, modList):
        ret = {}
        ability    = "Wisdom"
        abilityMod = stats[ability]

        ret['ability']    = ability
        ret['abilityMod'] = abilityMod

        bonus, source = modList.applyModifier("SpellSaveDC")

        bonus, source = modList.applyModifier("SpellSaveDC")
        source['Base'] = 8
        source['Prof.'] = profBonus
        source[ability] = abilityMod
        source = {k: v for k, v in sorted(source.items(), reverse=True, key=lambda item: item[1])}
        ret['saveDC'] = {'value': 8 + abilityMod + profBonus + bonus, 'source':source}

        bonus, source = modList.applyModifier("SpellAttack")
        source['Prof.'] = profBonus
        source[ability] = abilityMod
        source = {k: v for k, v in sorted(source.items(), reverse=True, key=lambda item: item[1])}
        ret['spellAttack'] = {'value':profBonus + abilityMod, 'source':source}

        ret['level'] = {}
        ret['level']['1'] = {}

        ret['level']['1']['slots'] = 3

        ret['level']['1']['list'] = {
            "Absorb Elements"   : {"source":"Ranger: Spellcasting"    , "timesPrepared":"-1", "description":""},
            "Cure Wounds"       : {"source":"Ranger: Spellcasting"    , "timesPrepared":"-1", "description":""},
            "Hunter\'s Mark"    : {"source":"Ranger: Spellcasting"    , "timesPrepared":"-1", "description":""},
            "Disguise Self"     : {"source":"Ranger: Gloom Stalker"   , "timesPrepared":"-1", "description":""},
            "Speak With Animals": {"source":"Ranger: Primal Awareness", "timesPrepared":"-1", "description":""},
        }

        return ret

    def getClassFeatures(self):
        return super().get5eClassFeatures()

    def getSubclassFeatures(self, url):
        return super().get5eSubclassFeatures(url)
