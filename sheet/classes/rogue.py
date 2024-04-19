from .classes import FifthEditionClass
from ..modifiers import ModifierList


class Rogue(FifthEditionClass):
    subclass = "Roguish Archetype"
    proficiencies = {
        "skills": ["Insight", "Stealth", "Performance", "Perception"],
        "languages": [],
        "armor": ["Light"],
        "weapons": ["Simple", "Hand crossbows", "Longswords", "Rapiers", "Shortswords"],
        "tools": ["Thieves' Tools"],
        "savingThrows": ["Intelligence", "Dexterity"],
    }
    expertise = {"skills": ["Insight", "Perception"]}

    def __init__(self):
        super().__init__(name="Rogue", hitDie="8", spellProgression="none")

    def appendModifiers(self, modList: ModifierList):
        super().appendModifiers(modList)

    def getConsumables(self, stats, proficiencyBonus):
        return []

    def getSpells(self, stats, profBonus, modList):
        return {}

    def getClassFeatures(self):
        return super().get5eClassFeatures()

    def getSubclassFeatures(self, url):
        return super().get5eSubclassFeatures(url)
