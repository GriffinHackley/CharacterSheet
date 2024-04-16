from .classes import FifthEditionClass
from ..modifiers import Modifier, ModifierList


class Bard(FifthEditionClass):
    subclass = "Bard College"
    proficiencies = {
        "skills": ["Perception", "Insight", "Performance"],
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

    def __init__(self, level, options, spellList):
        self.options = options
        self.subclassChoice = "Spirits"
        super().__init__(
            level,
            spellList,
            name="Bard",
            hitDie="8",
            spellProgression="full",
            primaryStat="Charisma",
        )

    def appendModifiers(self, modList: ModifierList):
        super().appendModifiers(modList)

    def getSubclassFeatureNames(self):
        match self.subclass:
            case "Spirits":
                return {
                    3: ["Guiding Whispers", "Spiritual Focus", "Tales from Beyond"],
                    6: ["Spirit Session"],
                    14: ["Mystical Connection"],
                }
            case _:
                error = "{} is not a valid subclass"
                raise Exception(error.format(self.subclass))
