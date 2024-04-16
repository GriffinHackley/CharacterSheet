from .classes import FifthEditionClass
from ..modifiers import ModifierList


class Artificer(FifthEditionClass):
    proficiencies = {
        "skills": ["Investigation", "Arcana"],
        "languages": [],
        "armor": ["Light", "Medium", "Shields"],
        "weapons": ["Simple"],
        "tools": ["Thieves' Tools", "Tinker's Tools"],
        "savingThrows": ["Constitution", "Intelligence"],
    }

    expertise = {"skills": []}

    def __init__(self, level, options, spellList):
        self.options = options
        super().__init__(
            level,
            spellList,
            name="Artificer",
            hitDie="8",
            spellProgression="half",
            primaryStat="Intelligence",
        )

    def appendModifiers(self, modList: ModifierList):
        super().appendModifiers(modList)

    def getConsumables(self, stats, proficiencyBonus):
        ret = {}

        ret["Magical Tinkering"] = {"uses": stats["Intelligence"]}

        return ret

    def getClassFeatures(self):
        subclassLevel = 3

        features = {
            1: ["Magical Tinkering", "Spellcasting"],
            2: ["Infuse Item"],
            3: ["The Right Tool for the Job"],
        }

        return super().getClassFeatures(features)

    def getSubclassFeatures(self, url):
        subclassName = self.options[feature].split(":")[1]
        subclassUrl = url + ":" + subclassName.replace(" ", "-")
        return super().get5eSubclassFeatures(url)
