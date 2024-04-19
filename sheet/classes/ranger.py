from .classes import FifthEditionClass
from ..modifiers import Modifier, ModifierList


class Ranger(FifthEditionClass):
    subclass = "Ranger Conclave"
    proficiencies = {
        "skills": ["Insight", "Stealth", "Survival"],
        "languages": ["Draconic", "Sylvan"],
        "armor": ["Light", "Medium"],
        "weapons": ["Simple", "Martial"],
        "tools": [],
        "savingThrows": ["Strength", "Dexterity"],
    }
    expertise = {"skills": ["Stealth"]}

    def __init__(self):
        self.subclassChoice = "Gloomstalker"
        super().__init__(
            name="Ranger",
            hitDie="10",
            spellProgression="half",
            primaryStat="Wisdom",
        )

    def appendModifiers(self, modList: ModifierList):
        super().appendModifiers(modList)

        modList.addModifier(Modifier(2, "ToHit-Ranged", "Archery Fighting Style"))
        modList.addModifier(Modifier("Wisdom", "Initiative", "Dread Ambusher"))

    def getConsumables(self, stats, proficiencyBonus):
        ret = {}

        ret["Favored Foe"] = {"uses": proficiencyBonus}

        return ret

    def getClassFeatures(self):
        return super().get5eClassFeatures()

    def getSubclassFeatures(self, url):
        return super().get5eSubclassFeatures(url)
