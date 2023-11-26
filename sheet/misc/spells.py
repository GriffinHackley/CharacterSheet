import json
from prettytable import PrettyTable
from bs4 import BeautifulSoup
import requests


class Spell:
    def __init__(self, name, source, castingType=""):
        self.name = name
        self.source = source
        self.scrapeSpell()

    def scrapeSpell(self):
        url = "http://dnd5e.wikidot.com/spell:" + self.name
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        heading = self.name.replace("-", " ").title()
        heading = soup.find("span", text=heading)

        spells = heading.findNext().findNext().findNext().findChildren()

        sourceBook = spells[1]
        text = spells[12]
        higherLevel = spells[14].next.next.next

        castingInfo = spells[4]
        castingTime = castingInfo.next.next.next
        range = castingTime.next.next.next.next.next
        components = range.next.next.next.next.next
        duration = components.next.next.next.next.next

        levelAndType = spells[2].text
        if levelAndType[0].isdigit():
            self.level = levelAndType[0]
            self.type = levelAndType.split(" ")[1].capitalize()
        else:
            self.level = "Cantrip"
            self.type = levelAndType.split(" ")[0]

        self.sourcebook = sourceBook.text
        self.text = text.text
        self.higherLevel = higherLevel.text

        self.castingTime = castingTime.text
        self.range = range.text
        self.components = components.text
        self.duration = duration.text

    def toJSON(self):
        return json.dumps(self.__dict__)


class SpellList:
    casterLevel = 0

    def __init__(self):
        slotTable = PrettyTable([str(i) for i in range(1, 10)])

        slotTable.add_rows(
            [
                # fmt: off
                [2, "-", "-", "-", "-", "-", "-", "-", "-"],
                [3, "-", "-", "-", "-", "-", "-", "-", "-"],
                [4,  2 , "-", "-", "-", "-", "-", "-", "-"],
                [4,  3 , "-", "-", "-", "-", "-", "-", "-"],
                [4,  3 ,  2 , "-", "-", "-", "-", "-", "-"],
                [4,  3 ,  3 , "-", "-", "-", "-", "-", "-"],
                [4,  3 ,  3 ,  1 , "-", "-", "-", "-", "-"],
                [4,  3 ,  3 ,  2 , "-", "-", "-", "-", "-"],
                [4,  3 ,  3 ,  3 ,  1 , "-", "-", "-", "-"],
                [4,  3 ,  3 ,  3 ,  2 , "-", "-", "-", "-"],
                [4,  3 ,  3 ,  3 ,  2 ,  1 , "-", "-", "-"],
                [4,  3 ,  3 ,  3 ,  2 ,  1 , "-", "-", "-"],
                [4,  3 ,  3 ,  3 ,  2 ,  1 ,  1 , "-", "-"],
                [4,  3 ,  3 ,  3 ,  2 ,  1 ,  1 , "-", "-"],
                [4,  3 ,  3 ,  3 ,  2 ,  1 ,  1 ,  1 , "-"],
                [4,  3 ,  3 ,  3 ,  2 ,  1 ,  1 ,  1 , "-"],
                [4,  3 ,  3 ,  3 ,  2 ,  1 ,  1 ,  1 ,  1 ],
                [4,  3 ,  3 ,  3 ,  3 ,  1 ,  1 ,  1 ,  1 ],
                [4,  3 ,  3 ,  3 ,  3 ,  2 ,  1 ,  1 ,  1 ],
                [4,  3 ,  3 ,  3 ,  3 ,  2 ,  2 ,  1 ,  1 ],
                # fmt: on
            ]
        )

        self.slotTable = slotTable
        self.spellList = {
            "Cantrip": [],
            "1": [],
            "2": [],
            "3": [],
            "4": [],
            "5": [],
            "6": [],
            "7": [],
            "8": [],
            "9": [],
        }

    def getSpellHeader(self, cls, stats, profBonus, modList):
        ability = cls.primaryStat
        abilityMod = stats[ability]

        ret = {}
        ret["ability"] = ability
        ret["abilityMod"] = abilityMod

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
        return ret

    def getSpellSlots(self):
        row = self.slotTable[self.casterLevel : self.casterLevel + 1].get_csv_string()
        level = row.split("\n")[1].split("-")[0].split(",")
        level.remove("")
        ret = {}
        for index, slots in enumerate(level):
            ret[index + 1] = slots
        return ret

    def addClass(self, cls):
        if cls.spellProgression == "full":
            self.casterLevel += cls.level
        for spell in cls.spellList:
            toAdd = Spell(spell, cls.name)
            self.spellList[toAdd.level].append(toAdd.toJSON())
        return

    def getSpellList(self):
        return self.spellList
        # ret = {}
        # ret["name"] = "Wizard"
        # ret["castingType"] = ["prepared", "ritual"]

        # ret["spells"] = {}
        # ret["spells"]["Cantrip"] = {}
        # ret["spells"]["1"] = {}
        # ret["spells"]["2"] = {}

        # ret["spells"]["1"]["slots"] = 4
        # ret["spells"]["2"]["slots"] = 2

        # cantrips = ["booming-blade"]
        # level1 = ["shield"]

        # for spell in level1:
        #     Spell(spell, "Wizard: Spellcasting")

        # ret["spells"]["Cantrip"]["list"] = {
        #     "Booming Blade": {
        #         "source": "Wizard: Spellcasting",
        #         "timesPrepared": "-1",
        #         "description": "",
        #     },
        #     "Mage Hand": {
        #         "source": "Wizard: Spellcasting",
        #         "timesPrepared": "-1",
        #         "description": "",
        #     },
        #     "Mind Sliver": {
        #         "source": "Wizard: Spellcasting",
        #         "timesPrepared": "-1",
        #         "description": "",
        #     },
        # }

        # ret["spells"]["1"]["list"] = {
        #     "Absorb Elements": {
        #         "source": "Wizard: Spellcasting",
        #         "timesPrepared": "1",
        #         "description": "",
        #     },
        #     "Detect Magic": {
        #         "source": "Wizard: Spellcasting",
        #         "timesPrepared": "-1",
        #         "description": "",
        #     },
        #     "Feather Fall": {
        #         "source": "Wizard: Spellcasting",
        #         "timesPrepared": "1",
        #         "description": "",
        #     },
        #     "Find Familiar": {
        #         "source": "Wizard: Spellcasting",
        #         "timesPrepared": "-1",
        #         "description": "",
        #     },
        #     "Identify": {
        #         "source": "Wizard: Spellcasting",
        #         "timesPrepared": "-1",
        #         "description": "",
        #     },
        #     "Jump": {
        #         "source": "Wizard: Spellcasting",
        #         "timesPrepared": "1",
        #         "description": "",
        #     },
        #     "Shield": {
        #         "source": "Wizard: Spellcasting",
        #         "timesPrepared": "1",
        #         "description": "",
        #     },
        #     "Silvery Barbs": {
        #         "source": "Wizard: Spellcasting",
        #         "timesPrepared": "1",
        #         "description": "",
        #     },
        # }

        # ret["spells"]["2"]["list"] = {
        #     "Invisibility": {
        #         "source": "Wizard: Spellcasting",
        #         "timesPrepared": "-1",
        #         "description": "",
        #     },
        #     "Shadow Blade": {
        #         "source": "Wizard: Spellcasting",
        #         "timesPrepared": "-1",
        #         "description": "",
        #     },
        # }

        # return ret
