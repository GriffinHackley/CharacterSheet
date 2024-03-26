from .classes import Class
from ..modifiers import Modifier, ModifierList


class Artificer(Class):
    proficiencies = {
        "skills": ["Investigation", "Perception"],
        "languages": [],
        "armor": ["Light", "Medium", "Shields"],
        "weapons": ["Simple"],
        "tools": ["Thieves'", "Tinker's"],
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
        return super().get5eClassFeatures()

    def getSubclassFeatures(self, url):
        return super().get5eSubclassFeatures(url)
