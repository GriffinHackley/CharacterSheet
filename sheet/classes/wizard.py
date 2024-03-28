from sheet.toggles import Toggle, ToggleList
from .classes import Class
from ..modifiers import Modifier, ModifierList


class Wizard(Class):
    proficiencies = {
        "skills": ["Arcana", "Investigation", "Performance"],
        "languages": [],
        "armor": ["Light"],
        "weapons": [
            "Daggers",
            "Darts",
            "Slings",
            "Quarterstaffs",
            "Light Crossbows",
            "Rapiers",
        ],
        "tools": [],
        "savingThrows": ["Intelligence", "Wisdom"],
    }
    expertise = {"skills": []}

    def __init__(self, level, options, spellList):
        self.options = options
        super().__init__(
            level,
            spellList,
            name="Wizard",
            hitDie="6",
            spellProgression="full",
            primaryStat="Intelligence",
        )

    def appendModifiers(self, modList: ModifierList):
        super().appendModifiers(modList)

    def getClassFeatures(self):
        return super().get5eClassFeatures()

    def getSubclassFeatures(self, url):
        return super().get5eSubclassFeatures(url)

    def getConsumables(self, stats, proficiencyBonus):
        ret = {}

        ret["Blade Song"] = {"uses": proficiencyBonus}

        return ret

    def getToggles(self, toggleList: ToggleList):
        bladesong = Toggle(
            "Blade Song",
            "Class Feature",
            [
                Modifier("Intelligence", "AC", source="Bladesong"),
                Modifier("Intelligence", "Concentration", source="Bladesong"),
                Modifier(10, "Speed", source="Bladesong"),
            ],
        )

        toggleList.addToggle(bladesong)
