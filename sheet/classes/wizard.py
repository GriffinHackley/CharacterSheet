from sheet.toggles import Toggle, ToggleList
from .classes import FifthEditionClass, Subclass
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

    def __init__(self):
        super().__init__(
            name="Wizard",
            hitDie="6",
            spellProgression="full",
            primaryStat="Intelligence",
        )

    def appendModifiers(self, modList: ModifierList):
        super().appendModifiers(modList)

    def getConsumables(self, stats, proficiencyBonus):
        ret = {}

        ret = ret | self.subclass.getConsumables(stats, proficiencyBonus)

        return ret

    def getToggles(self, toggleList: ToggleList):
        self.subclass.getToggles(toggleList)

    class Bladesinging(Subclass):
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

        def getConsumables(self, stats, proficiencyBonus):
            ret = {}

            ret["Blade Song"] = {"uses": proficiencyBonus}

            return ret

    class Abjurer(Subclass):
        i = 0
