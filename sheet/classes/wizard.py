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

    class Bladesinging(Subclass):
        def getFeatureFunctions(self):
            ret = {}

            ret["Bladesong"] = self.bladesong

            self.featureFunctions = ret

        def bladesong(self):
            bladesong = Toggle(
                "Bladesong",
                "Class Feature",
                [
                    Modifier("Intelligence", "AC", source="Bladesong"),
                    Modifier("Intelligence", "Concentration", source="Bladesong"),
                    Modifier(10, "Speed", source="Bladesong"),
                ],
            )

            self.toggles.append(bladesong)
            self.consumables["Bladesong"] = {"uses": "proficiencyBonus"}

    class Abjurer(Subclass):
        def getFeatureFunctions(self):
            ret = {}

            ret["Arcane Ward"] = self.arcaneWard

            self.featureFunctions = ret

        def arcaneWard(self):
            self.consumables["Arcane Ward"] = {"uses": "2*classLevel+Intelligence"}
