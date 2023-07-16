from .classes import FifthEditionClass
from ..modifiers import Modifier, ModifierList


class Bard(FifthEditionClass):
    proficiencies = {
        "skills": ["Perception", "Insight", "Performance"],
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
    expertise = {"skills": []}

    def __init__(self, level, options):
        self.options = options
        super().__init__(level, name="Bard", hitDie="8", spellProgression="full")

    def appendModifiers(self, modList: ModifierList):
        super().appendModifiers(modList)

    # TODO: make this the default
    def getClassFeatures(self):
        subclassLevel = 3

        features = {
            1: ["Spellcasting", "Bardic Inspiration"],
            2: ["Jack of All Trades", "Song of Rest", "Magical Inspiration"],
            3: ["Expertise"],
        }

        return super().getClassFeatures(features)

    def getSubclassFeatures(self, url):
        return super().get5eSubclassFeatures(url)

    def getSpells(self, stats, profBonus, modList):
        ability = "Charisma"
        ret = super().getSpells(stats, profBonus, modList, ability)
        ret["name"] = "Bard"
        ret["castingType"] = ["known", "ritual"]

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
            "Dissonant Whispers": {
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
