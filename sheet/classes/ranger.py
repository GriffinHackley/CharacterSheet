from .classes import FifthEditionClass, Subclass
from ..modifiers import Modifier, ModifierList


class Ranger(FifthEditionClass):
    subclass = "Ranger Conclave"
    proficiencies = {
        "skills": ["Insight", "Stealth", "Survival"],
        "languages": ["Draconic", "Sylvan"],
        "armor": ["Light", "Medium"],
        "weapons": ["Simple", "Martial"],
        "tools": [],
        "savingThrows": ["Strength", "Dexterity"],
    }
    expertise = {"skills": ["Stealth"]}

    def __init__(self):
        super().__init__(
            name="Ranger",
            hitDie="10",
            spellProgression="half",
            primaryStat="Wisdom",
        )

    def getFeatureFunctions(self):
        ret = {}

        ret["Favored Foe"] = self.favoredFoe
        ret["Fighting Style"] = self.fightingStyle

        self.featureFunctions = ret

    def favoredFoe(self):
        self.consumables["Favored Foe"] = {"uses": "proficiencyBonus"}

    def fightingStyle(self):
        self.modifiers.append(Modifier(2, "ToHit-Ranged", "Archery Fighting Style"))

    class GloomStalker(Subclass):
        def getFeatureFunctions(self):
            ret = {}

            ret["Dread Ambusher"] = self.dreadAmbusher

            self.featureFunctions = ret

        def dreadAmbusher(self):
            self.modifiers.append(Modifier("Wisdom", "Initiative", "Dread Ambusher"))
