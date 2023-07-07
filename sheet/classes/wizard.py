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
        super().__init__(level, name="Wizard", hitDie="6", edition="5e")

    def appendModifiers(self, modList: ModifierList):
        super().appendModifiers(modList)

    def getClassFeatures(self):
        return super().get5eClassFeatures()

    def getSubclassFeatures(self, url):
        return super().get5eSubclassFeatures(url)

    def getSpells(self, stats, profBonus, modList):
        ret = {}
        ability = "Intelligence"
        abilityMod = stats[ability]

        ret["ability"] = ability
        ret["abilityMod"] = abilityMod
        ret["castingType"] = ["prepared", "ritual"]

        bonus, source = modList.applyModifier("SpellSaveDC")
        source["Base"] = 8
        source["Prof."] = profBonus
        source[ability] = abilityMod
        source = {
            k: v
            for k, v in sorted(source.items(), reverse=True, key=lambda item: item[1])
        }
        ret["saveDC"] = {"value": 8 + abilityMod + profBonus + bonus, "source": source}

        bonus, source = modList.applyModifier("SpellAttack")
        source["Prof."] = profBonus
        source[ability] = abilityMod
        source = {
            k: v
            for k, v in sorted(source.items(), reverse=True, key=lambda item: item[1])
        }
        ret["spellAttack"] = {"value": profBonus + abilityMod, "source": source}

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
