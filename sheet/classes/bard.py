from .classes import FifthEditionClass
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
        self.subclassChoice = "Spirits"
        super().__init__(
            name="Bard",
            hitDie="8",
            spellProgression="full",
            primaryStat="Charisma",
        )

    def appendModifiers(self, modList: ModifierList):
        if self.level >= 2:
            mod = Modifier(
                "Proficiency/2", "Non-Proficient Ability Check", "Jack of All Trades"
            )
            modList.addModifier(mod)
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
