import re
import math
import requests
from .. import classes
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

class Class():
    def __init__(self, level, name, hitDie, edition, fort="poor", refl="poor", will="poor", bab="1/2"):
        self.edition = edition
        self.name = name
        self.hitDie = hitDie
        self.level = level
        if edition == "Pathfinder":
            self.fort = self.getSave(fort)
            self.refl = self.getSave(refl)
            self.will = self.getSave(will)
            self.bab = self.getBab(bab)
    
    def getBab(self, progression):
        if progression == "full":
            return self.level
        elif progression == "3/4":
            return math.floor(self.level*3/4)
        elif progression == "1/2":
            return math.floor(self.level/2)

    def getSave(self, progression):        
        if progression == "good":
            return 2+math.ceil((self.level-1)/2)
        elif progression == "poor":
            return math.floor((self.level)/3)

    def getConsumables(self, stats, proficiencyBonus):
        return []

    def appendModifiers(self, modList:ModifierList):
        if self.edition == "Pathfinder":
            modList.addModifier(Modifier(self.bab ,"untyped", 'ToHit'    , self.name+' BAB'))
            modList.addModifier(Modifier(self.fort,"untyped", 'Fortitude', self.name+' Fortitude'))
            modList.addModifier(Modifier(self.refl,"untyped", 'Reflex'   , self.name+' Reflex'))
            modList.addModifier(Modifier(self.will,"untyped", 'Will'     , self.name+' Will'))
    
    def addProficiencies(self, proficiencyList):
        proficiencyList['armor'] = proficiencyList['armor'] + self.proficiencies['armor']
        proficiencyList['weapons'] = proficiencyList['weapons'] + self.proficiencies['weapons']
        proficiencyList['languages'] = proficiencyList['languages'] + self.proficiencies['languages']
        if self.edition == "5e":
            proficiencyList['skills'] = proficiencyList['skills'] + self.proficiencies['skills']
            proficiencyList['tools'] = proficiencyList['tools'] + self.proficiencies['tools']
            proficiencyList['savingThrows'] = proficiencyList['savingThrows'] + self.proficiencies['savingThrows']

    def get5eClassFeatures(self):
        url = "http://dnd5e.wikidot.com/"+self.name
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        #Parse through the class table
        table = soup.find(attrs={"class":"wiki-content-table"})
        table = table.find_all("tr")

        levels = {}

        #Find feature Column
        headings = table[1].find_all("th")
        for i in range(len(headings)):
            if headings[i].contents[0] == "Features":
                featureIndex = i
                break

        for row in table:
            row = row.find_all("td")
            if len(row) > 0:
                #Get the level of current row
                currentLevel = row[0]
                currentLevel = currentLevel.text.split("s")[0]
                currentLevel = currentLevel.split("n")[0]
                currentLevel = currentLevel.split("r")[0]
                currentLevel = currentLevel.split("t")[0]

                if int(currentLevel) > self.level:
                    break

                #Get class features and add them to dict for this level
                features = row[featureIndex]
                features = features.text.split(", ")

                levels[currentLevel] = {}
                for feature in features:
                    levels[currentLevel][feature] = "Nothing"

        # Find all class features
        features = []
        for level in levels:
            for feature in levels[str(level)]:
                featureHeader = soup.find("h3", text=feature)
                
                if featureHeader == None:
                    continue

                if feature == "Ability Score Improvement":
                    continue

                featureText = []
                featureName = featureHeader.findNext()
                current = featureName
                featureName = featureName.text

                if feature in self.options.keys():

                    # Get subclass features
                    # TODO: These will all be grouped together
                    # TODO: Figure out a way to sort them with the main class features by level
                    if "subclass" in self.options[feature]:
                        subclassName = self.options[feature].split(":")[1]
                        subclassUrl = url + ":" + subclassName.replace(" ", "-")
                        features.update(self.getSubclassFeatures(subclassUrl))
                        continue

                    # If this feature was tagged as replaced, just skip it
                    if self.options[feature] == "replaced":
                        continue

                    # If feature is tagged as used, remove the optional from the feature name
                    if self.options[feature] == "used":
                        featureName = feature.replace(" (Optional)", "")
                        current = current.findNext()
                        
                        # Skip the line that talks about this feature replacing another
                        if "feature replaces" in current.text:
                            current = current.findNext()
                        
                        featureText.append({"type":"normal","text":current.text})  

                featureText = featureText + self.scrapeFeature(current, [], feature)

                features.append({'name': featureName, 'text':featureText})
        
        return features

    def get5eSubclassFeatures(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        featureHeaders = soup.findAll("h3")

        features = {}

        reg = re.compile(r'([0-9]+)(st|nd|rd|th) (level)')
                
        for featureHeader in featureHeaders:
            if featureHeader == None:
                continue

            if featureHeader.findNext().name == "a":
                continue

            featureName = featureHeader.findNext()
            current = featureName

            level = reg.search(current.findNext().text).group(1)
            
            if int(level) > self.level:
                continue

            featureText = self.scrapeFeature(current, [], featureName)
                
            features[featureName.text] = featureText

        return features

    def scrapeFeature(self, current, featureText, featureName):
        # Loop through html elements until you hit the next feature heading
        while not current.findNext().name == "h3":
            current = current.findNext()

            if len(featureText) >= 1:
                if current.text == featureText[len(featureText)-2]['text']:
                    current = current.findNext()
            
            #Handle list in feature
            if current.name == "ul":
                current = current.findNext()
                optionList = False
                while True:
                    if not featureName in self.options:
                        break
                    if current.name == "script":
                        break
                    if self.options[featureName] in current.text:
                        optionList = True
                        break
                    current = current.findNext().findNext()

                #If this feature is in options, filter it so it is only the option chosen
                if optionList:
                    text = current.text.replace(".", ":", 1)
                    choice = text.split(":")
                    featureText = featureText + [{"type":"heading","text":choice[0]},{"type":"normal","text":choice[1]}]
                    break
                else:
                    featureText.append({"type":"normal","text":current.text})
                    current = current.findNext()
            
            # When we get to divs that is the end of the features section      
            elif current.name == "div":
                break

            # Links get duplicated, so just skip them
            elif current.name == "a":
                continue
            
            # Strongs are put after the element they are in, so put it before instead
            elif current.name == "strong":
                featureText.insert(len(featureText)-1, {"type":"heading","text":current.text})
                continue
            
            # If its a table just take the whole table
            elif current.name == "table":
                featureText.append({"type":"table","text":current})
                break
            
            # Store headings as headings so they can be bolded
            elif current.name == "h6" or current.name == "h5":
                featureText.append({"type":"heading","text":current.text})
                current = current.findNext()
            
            # Store feature text
            else:
                featureText.append({"type":"normal","text":current.text})

        return featureText