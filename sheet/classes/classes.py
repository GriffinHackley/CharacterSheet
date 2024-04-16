import re
import math
import markdown
from .. import classes
from pathlib import Path
from bs4 import BeautifulSoup
from ..modifiers import Modifier, ModifierList


def allClasses():
    module = __import__("sheet")
    module = getattr(module, "classes")

    ret = {}
    for curr in classes.__all__:
        current = getattr(module, curr)
        ret[curr] = current

    return ret


def getClasses(levels, spellList):
    ret = []
    classes = allClasses()
    for charClass, level in levels.items():
        classModule = classes[charClass.lower()]
        cls = getattr(classModule, charClass)
        initClass = cls(level["level"], level["options"], spellList[charClass])
        ret.append(initClass)

    return ret


class Class:
    def __init__(self, level, spellList, name, hitDie, spellProgression, primaryStat):
        self.level = level
        self.spellList = spellList
        self.name = name
        self.hitDie = hitDie
        self.spellProgression = spellProgression
        self.primaryStat = primaryStat

        self.parseMd()

    def getConsumables(self, stats, proficiencyBonus):
        return []

    def appendModifiers(self, modList: ModifierList):
        return

    def addProficiencies(self, proficiencyList):
        # list(set()) converts removes duplicates
        proficiencyList["armor"] = list(
            set(proficiencyList["armor"] + self.proficiencies["armor"])
        )
        proficiencyList["weapons"] = list(
            set(proficiencyList["weapons"] + self.proficiencies["weapons"])
        )
        proficiencyList["languages"] = list(
            set(proficiencyList["languages"] + self.proficiencies["languages"])
        )

    def getToggles(self, toggleList):
        return {}

    def getSpells(self, stats, profBonus, modList, ability):
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

        # Loop through html elements until you hit the next feature heading
        while not current.findNext().name == "h3":
            current = current.findNext()

            if len(featureText) >= 1:
                if str(current) == featureText[len(featureText) - 2]["text"]:
                    current = current.findNext()

            # Handle list in feature
            if current.name == "ul":
                current = current.findNext()
                optionList = False
                while True:
                    if not featureName in self.options:
                        break
                    if current.name == "script":
                        break
                    if self.options[featureName] in str(current):
                        optionList = True
                        break
                    current = current.findNext().findNext()

                # If this feature is in options, filter it so it is only the option chosen
                if optionList:
                    text = str(current).replace(".", ":", 1)
                    choice = text.split(":")
                    featureText = featureText + [
                        {"type": "heading", "text": choice[0]},
                        {"type": "normal", "text": choice[1]},
                    ]
                    break
                else:
                    featureText.append({"type": "normal", "text": str(current)})
                    current = current.findNext()

            # When we get to divs that is the end of the features section
            elif current.name == "div":
                break

            # Links get duplicated, so just skip them
            elif current.name == "a":
                continue

            # Strongs are put after the element they are in, so put it before instead
            elif current.name == "strong":
                featureText.insert(
                    len(featureText) - 1, {"type": "heading", "text": str(current)}
                )
                continue

            # If its a table just take the whole table
            elif current.name == "table":
                featureText.append(
                    {"type": "table", "text": "tables have not been implemented yet"}
                )
                break

            # Store headings as headings so they can be bolded
            elif current.name == "h6" or current.name == "h5":
                featureText.append({"type": "heading", "text": str(current)})
                current = current.findNext()

            # Store feature text
            else:
                featureText.append({"type": "normal", "text": str(current)})

        return featureText


class FifthEditionClass(Class):
    def __init__(self, level, spellList, name, hitDie, spellProgression, primaryStat):
        super().__init__(level, spellList, name, hitDie, spellProgression, primaryStat)
        self.edition = "5e"

    def addProficiencies(self, proficiencyList):
        super().addProficiencies(proficiencyList)

        proficiencyList["skills"] = list(
            set(proficiencyList["skills"] + self.proficiencies["skills"])
        )
        proficiencyList["tools"] = list(
            set(proficiencyList["tools"] + self.proficiencies["tools"])
        )
        proficiencyList["savingThrows"] = list(
            set(proficiencyList["savingThrows"] + self.proficiencies["savingThrows"])
        )

    def getCasterLevel(self):
        if self.spellProgression == "full":
            return self.level

        if self.spellProgression == "half":
            return math.floor(self.level / 2)

        return 0

    def parseMd(self):
        relPath = "sources\\classes\\" + self.name + ".md"
        new_path = Path(__file__).parent.parent.parent / relPath
        with open(new_path) as f:
            markdownFile = f.read()
        html = markdown.markdown(markdownFile)
        htmlFile = BeautifulSoup(html, "html.parser")

        self.table = self.parseTable(htmlFile)

        self.features = self.getClassFeatures(htmlFile)

    def getClassFeatures(self, htmlFile):
        allFeatures = []
        modified = []
        regex = "\(([^\)]+)\)"

        for level in range(1, self.level - 1):
            for feature in self.table[level]["Features"]:

                # Look for features that improve as you level
                # If you find one, only get the text for the feature the first time
                # Skip it every other time
                match = re.search(regex, feature)
                if match:
                    feature = re.split(regex, feature)[0].strip(" ")
                    if feature in modified:
                        continue
                    else:
                        modified.append(feature)

                allFeatures.append(
                    {
                        "name": feature,
                        "text": self.getFeatureText(feature, htmlFile),
                    }
                )

        return allFeatures

    def parseTable(self, html):
        levels = {}

        table = (
            html.find("strong", text="Table- The {}".format(self.name)).findNext().text
        )

        table = self.mdTableToJSON(table)

        for i in range(1, 21):
            levels[i] = {"Features": table[i - 1]["Features"].split(",")}

        return levels

    # Taken from https://stackoverflow.com/questions/66185838/convert-markdown-table-to-json-with-python
    def mdTableToJSON(self, table):
        lines = table.split("\n")
        ret = []
        keys = []
        for i, l in enumerate(lines):
            if i == 0:
                keys = [_i.strip() for _i in l.split("|")]
            elif i == 1:
                continue
            else:
                ret.append(
                    {
                        keys[_i]: v.strip()
                        for _i, v in enumerate(l.split("|"))
                        if _i > 0 and _i < len(keys) - 1
                    }
                )
        return ret

    def getFeatureText(self, feature, soup):
        current = soup.find("h3", text=feature)

        if current == None:
            current = soup.find("h3", text=feature + " (Optional)")

        if current == None:
            raise Exception("Could not find {}".format(feature))

        featureText = []
        while not current.findNext().name == "h3":
            current = current.findNext()

            # Lists are weird for some reason, handle them as a special case
            if current.name == "ul":
                continue
            if current.name == "li":
                featureText.append(str(current))
                current = current.findNext()
                continue
            if current.name == "strong":
                current = current.findNext()

            featureText.append(str(current))

        featureText = "".join(featureText)
        return featureText


class PathfinderClass(Class):
    def __init__(self, level, name, hitDie, fort, refl, will, bab):
        super().__init__(level, name, hitDie, fort, refl, will, bab)
        self.edition = "Pathfinder"
        self.fort = self.getSave(fort)
        self.refl = self.getSave(refl)
        self.will = self.getSave(will)
        self.bab = self.getBab(bab)

    def getBab(self, progression):
        if progression == "full":
            return self.level
        elif progression == "3/4":
            return math.floor(self.level * 3 / 4)
        elif progression == "1/2":
            return math.floor(self.level / 2)

    def getSave(self, progression):
        if progression == "good":
            return 2 + math.ceil((self.level - 1) / 2)
        elif progression == "poor":
            return math.floor((self.level) / 3)

    def appendModifiers(self, modList: ModifierList):
        if self.edition == "Pathfinder":
            modList.addModifier(Modifier(self.bab, "ToHit", self.name + " BAB"))
            modList.addModifier(
                Modifier(self.fort, "Fortitude", self.name + " Fortitude")
            )
            modList.addModifier(Modifier(self.refl, "Reflex", self.name + " Reflex"))
            modList.addModifier(Modifier(self.will, "Will", self.name + " Will"))
