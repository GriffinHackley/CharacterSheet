from .classes import FifthEditionClass, Subclass
from ..modifiers import ModifierList


class Artificer(FifthEditionClass):
    subclass = "Artificer Specialist"
    proficiencies = {
        "skills": ["Investigation", "Arcana"],
        "languages": [],
        "armor": ["Light", "Medium", "Shields"],
        "weapons": ["Simple"],
        "tools": ["Thieves' Tools", "Tinker's Tools"],
        "savingThrows": ["Constitution", "Intelligence"],
    }

    expertise = {"skills": []}

    def __init__(self):
        super().__init__(
            name="Artificer",
            hitDie="8",
            spellProgression="half",
            primaryStat="Intelligence",
        )

    def getFeatureFunctions(self):
        ret = {}

        ret["Magical Tinkering"] = self.magicalTinkering

        self.featureFunctions = ret

    def magicalTinkering(self):
        self.consumables["Magical Tinkering"] = {"uses": "Intelligence"}

    class Artillerist(Subclass):
        def getConsumables(self, stats, proficiencyBonus):
            ret = {}

            ret["Free Eldritch Cannon"] = {"uses": 1}

            return ret
