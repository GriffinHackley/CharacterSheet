from .classes import FifthEditionClass, Subclass
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

    class Soulknife(Subclass):
        def getFeatureFunctions(self):
            ret = {}

            ret["Psionic Power"] = self.psionicPower

            self.featureFunctions = ret

        def psionicPower(self):
            self.consumables["Psionic Energy Dice"] = {"uses": "2*proficiencyBonus"}
