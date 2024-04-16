from sheet.toggles import Toggle, ToggleList
from .classes import FifthEditionClass
from ..modifiers import Modifier, ModifierList


class Wizard(FifthEditionClass):
    subclass = "Arcane Tradition"
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
