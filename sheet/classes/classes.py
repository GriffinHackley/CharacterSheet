import re
import math
import markdown

from .. import classes
from pathlib import Path
from bs4 import BeautifulSoup
from sheet.toggles import ToggleList
from ..modifiers import Modifier, ModifierList
from rest_framework.exceptions import APIException


def allClasses():
    module = __import__("sheet")
    module = getattr(module, "classes")

    ret = {}
    for curr in classes.__all__:
        current = getattr(module, curr)
        ret[curr] = current

    return ret


def allClassesJSON():
    ret = {}

    for name, info in allClasses().items():
        cls = getattr(info, name.title())()
        ret[name.title()] = {"features": cls.features, "starting": cls.starting}

    return ret


def getClasses(levels, spellList):
    ret = []
    classes = allClasses()
    for charClass, level in levels.items():
        classModule = classes[charClass.lower()]
        cls = getattr(classModule, charClass)
        initClass = cls()
        initClass.setLevel(level["level"])
        initClass.setOptions(level["options"])
        if spellList.get(charClass):
            initClass.setSpellList(spellList[charClass])
        ret.append(initClass)

    return ret


class Class:
    toggles = []
    modifiers = []
    consumables = {}
    featureFunctions = {}

    def __init__(self, name, hitDie, spellProgression, primaryStat):
        self.name = name
        self.hitDie = hitDie
        self.spellProgression = spellProgression
        self.primaryStat = primaryStat
        self.getFeatureFunctions()

    def setLevel(self, level):
        self.level = level

    def setSpellList(self, spellList):
        self.spellList = spellList

    def setOptions(self, options):
        self.options = options

        try:
            subclassInfo = self.options[self.subclass]
            subclassInfo["name"] = self.subclass
        except:
            raise Exception("Subclass section of options is malformed")

        try:
            choice = subclassInfo["choice"].replace(" ", "")
            self.subclass = getattr(self, choice)(subclassInfo)
        except:
            raise Exception(
                "Could not find a {} subclass by the name of {}".format(
                    self.name, subclassInfo.get("choice")
                )
            )

    # Run the corresponding funtion for all features
    def applyFeatures(self):
        for feature in self.features:
            functions = None

            # Get feature functions from either class or subclass
            if feature["name"] in self.featureFunctions:
                functions = self.featureFunctions
            if feature["name"] in self.subclass.featureFunctions:
                functions = self.subclass.featureFunctions

            if functions:
                functions[feature["name"]]()
        return

    def getFeatureFunctions(self):
        return

    def appendModifiers(self, modList: ModifierList):
        allMods = self.modifiers + self.subclass.modifiers

        modList.addModifierList(allMods)

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
        allToggles = self.toggles + self.subclass.toggles

        for toggle in allToggles:
            toggleList.addToggle(toggle)

        return {}

    def getConsumables(self, stats, proficiencyBonus):
        allConsumables = self.consumables | self.subclass.consumables

        for name, value in allConsumables.items():
            if type(value["uses"]) == int:
                continue

            # Convert to stats
            if value["uses"] in stats.keys():
                value["uses"] = stats[value["uses"]]

            if value["uses"] == "2*classLevel":
                value["uses"] = 2 * self.level

            if value["uses"] == "proficiencyBonus":
                value["uses"] = proficiencyBonus

            if value["uses"] == "2*proficiencyBonus":
                value["uses"] = 2 * proficiencyBonus

            if not type(value["uses"]) == int:
                raise APIException(
                    "Consumable uses must be an integer. Got {}".format(value["uses"])
                )

            allConsumables[name] = value

        return allConsumables

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

    def getExpertise(self):
        return self.subclass.getExpertise()


class Subclass:

    def __init__(self, subclassInfo):
        self.name = subclassInfo["name"]
        self.choice = subclassInfo["choice"]
        self.toggles = []
        self.modifiers = []
        self.consumables = {}
        self.featureFunctions = {}
        self.getFeatureFunctions()

    def getConsumables(self, stats, proficiencyBonus):
        return {}

    def getToggles(self, toggleList: ToggleList):
        return

    def getExpertise(self):
        return []

    def getFeatureFunctions(self):
        return


class FifthEditionClass(Class):
    def __init__(self, name, hitDie, spellProgression, primaryStat=None):
        super().__init__(name, hitDie, spellProgression, primaryStat)
        self.parseMd()
        self.edition = "5e"

    def setOptions(self, options):
        super().setOptions(options)
        self.features = self.getFeaturesToLevel()

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
        with open(new_path, "r", encoding="utf-8") as f:
            markdownFile = f.read()
        html = markdown.markdown(markdownFile)
        htmlFile = BeautifulSoup(html, "html.parser")

        self.table = self.parseTable(htmlFile)

        self.features = self.getAllClassFeatures(htmlFile)
        self.starting = self.getStarting(htmlFile)

    def parseTable(self, html):
        levels = {}

        table = (
            html.find("strong", text="Table- The {}".format(self.name)).findNext().text
        )

        table = self.mdTableToJSON(table)
        allFeatureNames = []

        for i in range(1, 21):
            stripped = []

            for feature in table[i - 1]["Features"].split(","):
                feature = feature.strip(" ")

                if feature == "-":
                    continue
                if feature in allFeatureNames:
                    continue
                if feature == "Ability Score Improvement":
                    continue

                ##TODO: Handle subclass levels
                # if feature == self.subclass:
                #     self.getSubclassFeatures(i)
                #     continue
                if feature == self.subclass + " feature":
                    continue

                stripped.append(feature)
                allFeatureNames.append(feature)

            levels[i] = {"Features": stripped}

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

    def getAllClassFeatures(self, htmlFile):
        allFeatures = {}
        modified = []
        regex = "\(([^\)]+)\)"

        for level in range(1, 21):
            currentLevel = []
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
                if "Improvement" in feature:
                    feature = feature.split(" Improvement")[0]
                    if not feature in modified:
                        modified.append(feature)
                    continue

                currentLevel.append(
                    {
                        "name": feature,
                        "text": self.getFeatureText(feature, htmlFile),
                    }
                )
            allFeatures[level] = currentLevel

        return allFeatures

    def getFeaturesToLevel(self):
        features = []

        relPath = "sources\\subclasses\\{}\\{}.md".format(
            self.name, self.subclass.choice
        )
        new_path = Path(__file__).parent.parent.parent / relPath
        with open(new_path, "r", encoding="utf-8") as f:
            markdownFile = f.read()
        html = markdown.markdown(markdownFile)
        htmlFile = BeautifulSoup(html, "html.parser")

        for level in range(1, self.level + 1):
            for feature in self.features[level]:
                if feature["name"] == self.subclass.name:
                    features = features + self.getSubclassFeature(htmlFile, level)
                else:
                    features = features + [feature]

        return features

    def getFeatureText(self, feature, soup, omitFirst=False):
        current = soup.find("h3", text=feature)

        if current == None:
            current = soup.find("h3", text=feature + " (Optional)")

        if current == None:
            raise Exception("Could not find the {} feature".format(feature))

        featureText = []
        while current.findNext() and not current.findNext().name == "h3":
            current = current.findNext()

            # Lists are weird for some reason, handle them as a special case
            if current.name == "em":
                continue
            if current.name == "ul":
                continue
            if current.name == "li":
                featureText.append(str(current))
                current = current.findNext()
                continue
            if current.name == "strong":
                current = current.findNext()

            featureText.append(str(current))

        if omitFirst:
            featureText = featureText[2:]

        featureText = "".join(featureText)
        return featureText

    def getSubclassFeature(self, htmlFile, level):
        allFeatures = htmlFile.findAll("em")

        currentLevel = []

        for feature in allFeatures:
            if feature.text[:-2] == str(level):
                currentLevel.append(feature)

        ret = []

        for feature in currentLevel:
            name = feature.findPrevious().findPrevious().findPrevious().text
            ret.append(
                {
                    "name": name,
                    "text": self.getFeatureText(name, htmlFile, omitFirst=True),
                }
            )

        return ret

    def getStarting(self, htmlFile):
        ret = {}

        ret["Armor"] = htmlFile.find("strong", text="Armor:").next_sibling[1:]
        ret["Weapons"] = htmlFile.find("strong", text="Weapons:").next_sibling[1:]
        ret["Tools"] = self.convertToolsToDict(
            htmlFile.find("strong", text="Tools:").next_sibling
        )

        return ret

    def convertToolsToDict(self, string):
        ret = {"choices": {}, "defaults": []}
        entries = string[1:].split(", ")
        for entry in entries:
            if " of your choice" in entry:
                split = entry.split(" of your choice")[0]
                if " of " in split:
                    (number, toolType) = split.split(" of ")
                else:
                    (number, toolType) = split.split(" ", 1)
                number = number.split(" type")[0]
                number = self.convertStringToInt(number)
                ret["choices"][toolType] = number
            else:
                ret["defaults"].append(entry)
        return ret

    def convertStringToInt(self, string):
        string = string.lower()

        match string:
            case "one":
                return 1
            case "two":
                return 2
            case "three":
                return 3
            case "four":
                return 4
            case "five":
                return 5

    def toJSON(self):
        ret = {}

        ret[self.name] = {"features": self.features}

        return ret


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
