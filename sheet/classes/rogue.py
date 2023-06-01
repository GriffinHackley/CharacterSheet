from .classes import Class
from ..modifiers import Modifier, ModifierList

class Rogue(Class):
    proficiencies = {'skills': ['Insight', 'Stealth', 'Performance', 'Perception'], 'languages':[], 'armor': ['Light'], 'weapons':['Simple', 'Hand crossbows', 'Longswords', 'Rapiers', 'Shortswords'], 'tools':["Thieves' Tools"], 'savingThrows':['Intelligence', 'Dexterity']}
    expertise = {'skills': ['Insight', 'Perception']}

    def __init__(self, level, options):
        self.options = options
        super().__init__(level, name="Rogue", hitDie='8', edition="5e")

    def appendModifiers(self, modList: ModifierList):
        super().appendModifiers(modList)

    def getConsumables(self, stats, proficiencyBonus):
        return {}
    
    def getSpells(self, stats, profBonus, modList):
        ret = {}
        ability    = "Wisdom"
        abilityMod = stats[ability]

        ret['ability']    = ability
        ret['abilityMod'] = abilityMod

        bonus, source = modList.applyModifier("SpellSaveDC")

        bonus, source = modList.applyModifier("SpellSaveDC")
        
        ret['saveDC'] = {'value': 8 + abilityMod + profBonus + bonus, 'source':source}

        ret['spellAttack'] = {'value':profBonus + abilityMod, 'source':source}

        ret['level'] = {}

        return ret

    def getClassFeatures(self):
        return super().get5eClassFeatures()

    def getSubclassFeatures(self, url):
        return super().get5eSubclassFeatures(url)