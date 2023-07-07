from .classes import Class
from ..modifiers import Modifier, ModifierList


class Bard(Class):
    proficiencies = {
        "skills": ["Perception", "Insight", "Performance"],
        "languages": [],
        "armor": ["Light"],
        "weapons": [
            "Simple weapons",
            "hand crossbows",
            "longswords",
            "rapiers",
            "shortswords",
        ],
        "tools": ["Bagpipes", "Lute", "Pan Flute"],
        "savingThrows": ["Dexterity", "Charisma"],
    }
    expertise = {"skills": []}

    def __init__(self, level, options):
        self.options = options
        super().__init__(level, name="Bard", hitDie="8", edition="5e")

    def appendModifiers(self, modList: ModifierList):
        super().appendModifiers(modList)

    def getClassFeatures(self):
        return super().get5eClassFeatures()

    def getSubclassFeatures(self, url):
        return super().get5eSubclassFeatures(url)

    def getSpells(self, stats, profBonus, modList):
        ret = {}
        ability = "Charisma"
        abilityMod = stats[ability]

        ret["ability"] = ability
        ret["abilityMod"] = abilityMod
        ret["castingType"] = ["known", "ritual"]

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
        # ret["spells"]['2'] = {}

        ret["spells"]["1"]["slots"] = 3
        # ret["spells"]['2']['slots'] = 2

        ret["spells"]["Cantrip"]["list"] = {
            "Mage Hand": {
                "source": "Bard: Spellcasting",
                "timesPrepared": "-1",
                "description": "",
            },
            "Vicious Mockery": {
                "source": "Bard: Spellcasting",
                "timesPrepared": "-1",
                "description": "",
            },
        }

        ret["spells"]["1"]["list"] = {
            "Bane": {
                "source": "Bard: Spellcasting",
                "timesPrepared": "-1",
                "description": "",
            },
            "Detect Magic": {
                "source": "Bard: Spellcasting",
                "timesPrepared": "-1",
                "description": "",
            },
            "Dissonant Whiespers": {
                "source": "Bard: Spellcasting",
                "timesPrepared": "-1",
                "description": "",
            },
            "Silvery Barbs": {
                "source": "Bard: Spellcasting",
                "timesPrepared": "-1",
                "description": "",
            },
            "Tasha's Hideous Laughter": {
                "source": "Bard: Spellcasting",
                "timesPrepared": "-1",
                "description": "",
            },
            "Unseen Srevant": {
                "source": "Bard: Spellcasting",
                "timesPrepared": "-1",
                "description": "",
            },
        }

        # ret["spells"]['2']['list'] = {
        # }

        return ret
