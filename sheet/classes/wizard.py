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

    def __init__(self, level, options):
        self.options = options
        super().__init__(level, name="Wizard", hitDie="6", spellProgression="full")

    def appendModifiers(self, modList: ModifierList):
        super().appendModifiers(modList)

    def getClassFeatures(self):
        return super().get5eClassFeatures()

    def getSubclassFeatures(self, url):
        return super().get5eSubclassFeatures(url)

    def getSpells(self, stats, profBonus, modList):
        ability = "Intelligence"
        ret = super().getSpells(stats, profBonus, modList, ability)
        ret["name"] = "Wizard"
        ret["castingType"] = ["prepared", "ritual"]

        ret["spells"] = {}
        ret["spells"]["Cantrip"] = {}
        ret["spells"]["1"] = {}
        ret["spells"]["2"] = {}

        ret["spells"]["1"]["slots"] = 4
        ret["spells"]["2"]["slots"] = 2

        ret["spells"]["Cantrip"]["list"] = {
            "Booming Blade": {
                "source": "Wizard: Spellcasting",
                "timesPrepared": "-1",
                "description": "",
            },
            "Mage Hand": {
                "source": "Wizard: Spellcasting",
                "timesPrepared": "-1",
                "description": "",
            },
            "Mind Sliver": {
                "source": "Wizard: Spellcasting",
                "timesPrepared": "-1",
                "description": "",
            },
        }

        ret["spells"]["1"]["list"] = {
            "Absorb Elements": {
                "source": "Wizard: Spellcasting",
                "timesPrepared": "1",
                "description": "",
            },
            "Detect Magic": {
                "source": "Wizard: Spellcasting",
                "timesPrepared": "-1",
                "description": "",
            },
            "Feather Fall": {
                "source": "Wizard: Spellcasting",
                "timesPrepared": "1",
                "description": "",
            },
            "Find Familiar": {
                "source": "Wizard: Spellcasting",
                "timesPrepared": "-1",
                "description": "",
            },
            "Identify": {
                "source": "Wizard: Spellcasting",
                "timesPrepared": "-1",
                "description": "",
            },
            "Jump": {
                "source": "Wizard: Spellcasting",
                "timesPrepared": "1",
                "description": "",
            },
            "Shield": {
                "source": "Wizard: Spellcasting",
                "timesPrepared": "1",
                "description": "",
            },
            "Silvery Barbs": {
                "source": "Wizard: Spellcasting",
                "timesPrepared": "1",
                "description": "",
            },
        }

        ret["spells"]["2"]["list"] = {
            "Invisibility": {
                "source": "Wizard: Spellcasting",
                "timesPrepared": "-1",
                "description": "",
            },
            "Shadow Blade": {
                "source": "Wizard: Spellcasting",
                "timesPrepared": "-1",
                "description": "",
            },
        }

        return ret
