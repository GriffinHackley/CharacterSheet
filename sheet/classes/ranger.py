from .classes import Class
from ..modifiers import Modifier, ModifierList


class Ranger(Class):
    proficiencies = {
        "skills": ["Insight", "Stealth", "Survival"],
        "languages": ["Draconic", "Sylvan"],
        "armor": ["Light", "Medium"],
        "weapons": ["Simple", "Martial"],
        "tools": [],
        "savingThrows": ["Strength", "Dexterity"],
    }
    expertise = {"skills": ["Stealth"]}

    def __init__(self, level, options):
        self.options = options
        super().__init__(level, name="Ranger", hitDie="10", spellProgression="half")

    def appendModifiers(self, modList: ModifierList):
        super().appendModifiers(modList)

        modList.addModifier(Modifier(2, "ToHit-Ranged", "Archery Fighting Style"))
        modList.addModifier(Modifier("Wisdom", "Initiative", "Dread Ambusher"))

    def getConsumables(self, stats, proficiencyBonus):
        ret = {}

        ret["Favored Foe"] = {"uses": proficiencyBonus}

        return ret

    def getSpells(self, stats, profBonus, modList):
        ability = "Wisdom"
        ret = super().getSpells(stats, profBonus, modList, ability)
        ret["castingType"] = ["known"]

        ret["spells"] = {}
        ret["spells"]["1"] = {}

        ret["spells"]["1"]["slots"] = 3

        ret["spells"]["1"]["list"] = {
            "Absorb Elements": {
                "source": "Ranger: Spellcasting",
                "timesPrepared": "-1",
                "description": "",
            },
            "Cure Wounds": {
                "source": "Ranger: Spellcasting",
                "timesPrepared": "-1",
                "description": "",
            },
            "Hunter's Mark": {
                "source": "Ranger: Spellcasting",
                "timesPrepared": "-1",
                "description": "",
            },
            "Disguise Self": {
                "source": "Ranger: Gloom Stalker",
                "timesPrepared": "-1",
                "description": "",
            },
            "Speak With Animals": {
                "source": "Ranger: Primal Awareness",
                "timesPrepared": "-1",
                "description": "",
            },
        }

        return ret

    def getClassFeatures(self):
        return super().get5eClassFeatures()

    def getSubclassFeatures(self, url):
        return super().get5eSubclassFeatures(url)
