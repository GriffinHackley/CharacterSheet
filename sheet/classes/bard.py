from .classes import FifthEditionClass
from ..modifiers import Modifier, ModifierList


class Bard(FifthEditionClass):
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
        self.subclass = "Spirits"
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

    # TODO: make this the default
    # def getClassFeatures(self):
    #     features = {
    #         1: ["Spellcasting", "Bardic Inspiration"],
    #         2: ["Jack of All Trades", "Song of Rest", "Magical Inspiration"],
    #         3: ["Expertise"],
    #         4: ["Bardic Versatility"],
    #         5: [],
    #         6: [],
    #         7: [],
    #         8: [],
    #         9: [],
    #         11: [],
    #         12: [],
    #         13: [],
    #         14: [],
    #         15: [],
    #         16: [],
    #         17: [],
    #         18: [],
    #         19: [],
    #         20: [],
    #     }

    #     # classFeatures = super().getClassFeatures(features)

    #     # Add Subclass features
    #     # subclassLevel = [3, 6, 14]
    #     # subclassFeatureNames = self.getSubclassFeatureNames()
    #     # subclassFeatures = super().getSubclassFeatures(subclassFeatureNames)
    #     # for level in subclassLevel:
    #     #     features[level] += subclassFeatureNames[level]

    #     return classFeatures

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
