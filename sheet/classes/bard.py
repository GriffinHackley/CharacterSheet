from .classes import FifthEditionClass, Subclass
from ..modifiers import Modifier, ModifierList


class Bard(FifthEditionClass):
    subclass = "Bard College"
    proficiencies = {
        "skills": ["Perception", "Insight", "Persuasion"],
        "languages": [],
        "armor": ["Light"],
        "weapons": [
            "Simple weapons",
            "Hand Crossbows",
            "Longswords",
            "Rapiers",
            "Shortswords",
        ],
        "tools": ["Bagpipes", "Lute", "Pan Flute"],
        "savingThrows": ["Dexterity", "Charisma"],
    }
    expertise = {"skills": ["Perception", "Persuasion"]}

    def __init__(self):
        super().__init__(
            name="Bard",
            hitDie="8",
            spellProgression="full",
            primaryStat="Charisma",
        )

    def getFeatureFunctions(self):
        ret = {}

        ret["Jack of All Trades"] = self.jackOfAllTrades

        self.featureFunctions = ret

    def jackOfAllTrades(self):
        self.modifiers.append(
            Modifier(
                "Proficiency/2", "Non-Proficient Ability Check", "Jack of All Trades"
            )
        )

    class Spirits(Subclass):
        i = 0
