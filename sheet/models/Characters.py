import math
import json

from django.db import models
from django.template.defaulttags import register

from ..races import races
from ..classes import classes
from ..toggles import ToggleList
from ..modifiers import ModifierList
from ..lists import Ability, combat_list
from rest_framework.exceptions import APIException


class Character(models.Model):
    def create(cls):
        pass

    @register.filter
    def get_item(dictionary, key):
        return dictionary.get(key)

    @property
    def attribute(self):
        return self._attribute

    @attribute.setter
    def attribute(self, value):
        self._attribute = value

    @attribute.deleter
    def attribute(self):
        del self._attribute

    def __str__(self):
        return self.name

    baseStats = models.CharField(max_length=240)

    name = models.CharField(max_length=240)

    charClass = models.CharField(max_length=500)
    level = models.IntegerField()
    spellList = models.CharField(max_length=500)
    race = models.CharField(max_length=500)
    background = models.CharField(max_length=240)
    feats = models.CharField(max_length=240)
    playerName = models.CharField(max_length=240)
    alignment = models.CharField(max_length=240)
    config = models.CharField(max_length=240)
    traits = models.CharField(max_length=240)
    skillRanks = models.CharField(max_length=240)

    weapon = models.CharField(max_length=1000)
    equipment = models.CharField(max_length=500)

    flavor = models.CharField(max_length=10000)

    accentColor = models.CharField(max_length=240)

    def fromCharacter(self, character):
        self.name = character.name
        self.baseStats = character.baseStats
        self.level = character.level
        self.alignment = character.alignment
        self.playerName = character.playerName

        try:
            self.charClass = json.loads(character.charClass)
            self.spellList = json.loads(character.spellList)
            self.race = json.loads(character.race)
            self.feats = json.loads(character.feats)
            self.background = json.loads(character.background)
            self.config = json.loads(character.config)
            self.weapon = json.loads(character.weapon)
            self.equipment = json.loads(character.equipment)
            self.flavor = json.loads(character.flavor)
            self.accentColor = json.loads(character.accentColor)

        except:
            raise APIException("Invalid Character JSON")

        return self

    def exportCharacter(self):
        ret = {}

        ret["config"] = self.getConfig()
        ret["header"] = self.getHeader()
        ret["attributes"] = self.getAttributes()
        ret["saves"] = self.saves
        ret["skills"] = self.skills
        ret["combat"] = self.combat
        ret["consumables"] = self.getConsumables()
        ret["features"] = self.features
        ret["equipment"] = self.equipment
        ret["proficiencies"] = self.proficiencies
        ret["spells"] = self.spells
        ret["flavor"] = self.flavor
        ret["toggles"] = self.toggles.toJson()

        # cache.set(self.name, ret)

        ret["graph"] = self.calculateGraph()

        return json.dumps(ret)

    def getHeader(self):
        ret = {}

        ret["Class and Level"] = {}
        for cls in self.charClass:
            ret["Class and Level"][cls.name] = cls.level

        ret["Character Name"] = self.name
        ret["Background"] = self.background.name
        ret["Race"] = self.race.name
        ret["Alignment"] = self.alignment
        ret["Player Name"] = self.playerName

        return ret

    def getConfig(self):
        ret = {}

        ret["level"] = self.level
        ret["edition"] = self.config["edition"]
        ret["accentColors"] = self.accentColor

        return ret

    def getAttributes(self):
        ret = []

        for ability, value in self.abilityScores.items():
            ret.append(
                {
                    "name": ability,
                    "score": value["value"],
                    "mod": self.abilityMod[ability],
                    "source": value["source"],
                }
            )

        return ret

    def build(self):
        self.graph = None
        self.toggles = ToggleList()
        self.modList = ModifierList()
        self.getTotalLevel()
        self.getBaseModifiers()
        self.calculateStats()
        self.getConditionalModifiers()
        self.cleanModifiers()
        self.saves = self.calculateSaves()
        self.features = self.getFeatures()
        self.skills = self.calculateSkills()
        self.combat = self.calculateCombat()
        self.equipment = self.getEquipment()
        self.spells = self.getSpells()
        self.proficiencies = self.cleanProficiencies()

    def getBaseModifiers(self):
        self.initModifiers()
        self.applyRace()
        self.applyBackground()
        self.applyClass()
        self.applyFeats()

    def getConditionalModifiers(self):
        self.applySpells()
        self.applyToggles()

    def applyToggles(self):
        if not hasattr(self, "activeToggles"):
            return

        for toggle, value in self.activeToggles.items():
            if not self.toggles.isInList(toggle):
                raise APIException(
                    "{} was not found in the toggle list for this character".format(
                        toggle
                    )
                )

            if value:
                tempToggle = self.toggles.getFullList()[toggle]
                tempToggle.isUsed = True
                modifiers = tempToggle.modifiers
                self.modList.addModifierList(modifiers)

    def cleanModifiers(self):
        self.modList.cleanModifiers(self.abilityMod, self.profBonus)

    def getTotalLevel(self):
        totalLevel = 0

        for cls, data in self.charClass.items():
            totalLevel += data["level"]
        self.totalLevel = totalLevel

    def calculateStats(self):
        stats = self.decodeStats()

        self.abilityScores = {}
        self.abilityMod = {}

        for ability in Ability:
            self.abilityScores[ability.name] = {}
            base = int(stats[ability.value])
            bonus, source = self.modList.applyModifier(ability.name)

            # Add base score and sort sources from highest to lowest
            source["Base"] = base
            source = {
                k: v
                for k, v in sorted(
                    source.items(), reverse=True, key=lambda item: item[1]
                )
            }

            self.abilityScores[ability.name]["value"] = base + bonus
            self.abilityScores[ability.name]["source"] = source
            self.abilityMod[ability.name] = (
                math.floor(self.abilityScores[ability.name]["value"] / 2) - 5
            )

    def calculateCombat(self):
        ret = {}

        ret["Initiative"] = self.calculateInit()
        ret["Speed"] = self.calculateSpeed()
        ret["HP"] = self.calculateHP()
        ret["Armor Class"] = self.calculateAC()
        ret["Attacks"] = self.calculateAttacks()
        ret["hitDice"] = "{}d{}".format(self.level, self.hitDie)
        ret["config"] = {"name": self.name, "edition": self.config["edition"]}

        return ret

    def getConsumables(self):
        ret = {}

        for cls in self.charClass:
            ret.update(cls.getConsumables(self.abilityMod, self.profBonus))

        ret.update(self.race.getConsumables(self.abilityMod, self.profBonus))

        return ret

    def applyRace(self):
        options = self.race["options"]
        self.race = races.getRace(self.race["name"])()
        self.race.setOptions(options)
        self.race.setLevel(self.totalLevel)
        self.race.appendModifiers(self.modList)
        self.race.addProficiencies(self.proficiencies)
        self.feats.update(self.race.getFeat())

    def applyClass(self):
        self.charClass = classes.getClasses(self.charClass, self.spellList)

        for cls in self.charClass:
            cls.applyFeatures()
            cls.appendModifiers(self.modList)
            cls.addProficiencies(self.proficiencies)
            cls.getToggles(self.toggles)
            self.hitDie = cls.hitDie

    def applyFeats(self, featList):
        ret = {}

        for name, feat in self.feats.items():
            source = feat["source"]

            newFeat = featList[name]()
            newFeat.setSource(source)

            if feat.get("options", None):
                options = feat["options"]
                newFeat.setOptions(options)

            newFeat.getModifiers(self.modList)

            ret[name] = newFeat

        self.feats = ret

    def applySpells(self):
        return

    def calculateInit(self):
        modifier, source = self.modList.applyModifier("Initiative")

        # TODO: JoaT should only apply if prof. bonus is not already added
        # which it can be with something like harengons hare-trigger
        newModifier, newSource = self.modList.applyModifier(
            "Non-Proficient Ability Check"
        )

        modifier = modifier + newModifier
        source = source | newSource

        init = combat_list["Initiative"]
        ability = self.convertEnum(init["ability"])
        bonus = self.abilityMod[ability]
        source[ability] = self.abilityMod[ability]

        bonus += modifier

        source = {
            k: v
            for k, v in sorted(source.items(), reverse=True, key=lambda item: item[1])
        }

        return {"value": bonus, "source": source}

    def calculateSpeed(self):
        bonus, source = self.modList.applyModifier("Speed")

        source["Base"] = self.race.speed
        speed = self.race.speed

        speed += bonus

        source = {
            k: v
            for k, v in sorted(source.items(), reverse=True, key=lambda item: item[1])
        }

        return {"value": speed, "source": source}

    def calculateHP(self):
        # Level one max die
        die = int(self.hitDie)

        # Average roll of hitdie
        hpPerLevel = (die / 2) + 1
        die += (self.level - 1) * hpPerLevel

        # Add Constitution
        hpPerLevel = self.abilityMod["Constitution"]
        die += self.level * hpPerLevel

        return int(die)

    def calculateCritChance(self, attacks):
        # Nail
        # main = self.critChance(attacks['Main Kukri'])
        # off = self.critChance(attacks['Off-Hand Kukri'])

        # none = (1-main)*(1-off)
        # one = 1-none
        # two = main*off

        # return (none*100, one*100, two*100)

        # Myriil
        # Chance of not critting on an attack
        if "advantage" in self.toggles and self.toggles["advantage"]:
            baseChance = pow(0.95, 3)
        else:
            baseChance = 0.05

        if "dreadAmbusher" in self.toggles and self.toggles["dreadAmbusher"]:
            # chance of not critting on either attack
            overall = pow(baseChance, 2)
        else:
            # chance of not critting on only first attack
            overall = baseChance

        return {"one": 1 - baseChance, "multiple": 1 - overall}

    def critChance(self, attack):
        critRange = attack["critRange"]
        critRange = int(critRange.split("-")[0])
        critChance = (21 - critRange) / 20
        return critChance

    def attackInit(self, weapon):
        # Add weapon die to damage die
        allDie, dieSource = self.modList.getDieModifier(weapon["tags"], self.spellList)

        dieSource["Weapon Die"] = weapon["damageDie"]
        damageDie = weapon["damageDie"]
        [number, size] = damageDie.split("d")
        if size in allDie.keys():
            allDie[size] = allDie[size] + int(number)
        else:
            allDie[size] = int(number)

        ret = {}
        # ret["toHit"] = {"value": toHit, "source": toHitSource}
        # ret["damageMod"] = {"value": damageMod, "source": damageSource}
        ret["allDie"] = {"value": allDie, "source": dieSource}

        return ret

    def calculateAttack(self, attack, weapon):
        toHit = attack["toHit"]["value"]
        toHitSource = attack["toHit"]["source"]

        damageMod = attack["damageMod"]["value"]
        damageSource = attack["damageMod"]["source"]

        allDie = attack["allDie"]
        dieSource = attack["allDie"]["source"]

        # Format Damage Dice
        firstLetter = True
        sortedDieSize = reversed(
            sorted(list(allDie["value"].keys()))
        )  # Order from highest to smallest die size
        criticalDamage = 0
        averageDamage = 0
        for dieSize in sortedDieSize:
            damageDie = allDie["value"][dieSize]

            if self.toggles.defaultToggles["Critical"].isUsed:
                if (
                    self.config["critType"] == "doubleDice"
                    or self.config["critType"] == "doubleAll"
                ):
                    allDie["source"]["Critical"] = str(damageDie) + "d" + str(dieSize)
                    damageDie = damageDie * 2

            if firstLetter:
                firstLetter = False
                damageDice = str(damageDie) + "d" + dieSize
            else:
                damageDice = damageDice + "+" + str(damageDie) + "d" + dieSize

            # Calculate critical damage
            if self.config["critType"] == "maxDie":
                criticalDamage += allDie["value"][dieSize] * int(dieSize)
            elif self.config["critType"] == "doubleDice":
                criticalDamage += allDie["value"][dieSize] * ((int(dieSize) / 2) + 0.5)
            elif self.config["critType"] == "doubleDice":
                pass
            averageDamage += allDie["value"][dieSize] * ((int(dieSize) / 2) + 0.5)

        averageDamage += damageMod

        # If critical, add extra critical damage
        if self.toggles.defaultToggles["Critical"].isUsed:
            if self.config["critType"] == "maxDie":
                damage = (
                    damageDice
                    + f"+{int(damageMod+criticalDamage)} "
                    + weapon["damageType"]
                )
            elif self.config["critType"] == "doubleAll":
                damage = damageDice + f"+{2*damageMod} " + weapon["damageType"]
            else:
                damage = damageDice + f"+{damageMod} " + weapon["damageType"]
        else:
            damage = damageDice + f"+{damageMod} " + weapon["damageType"]

        toHitSource = {
            k: v
            for k, v in sorted(
                toHitSource.items(), reverse=True, key=lambda item: item[1]
            )
        }
        damageSource = {
            k: v
            for k, v in sorted(
                damageSource.items(), reverse=True, key=lambda item: item[1]
            )
        }
        dieSource = dict(reversed(sorted(dieSource.items(), key=lambda x: x[1])))

        dieSource.update(damageSource)

        ret = {}
        ret["name"] = weapon["name"]
        ret["toHit"] = {"value": toHit, "source": toHitSource}
        ret["damage"] = {"value": damage, "source": dieSource}
        ret["damageMod"] = damageMod
        ret["averageDamage"] = averageDamage
        ret["bonusCritDamage"] = criticalDamage

        return ret

    def calculateGraph(self):
        allToggles = self.toggles.getFullList()

        if hasattr(self, "activeToggles"):
            for toggle, value in self.activeToggles.items():
                allToggles[toggle].isUsed = value

        if allToggles["Advantage"].isUsed:
            if "Elven Accuracy" in self.feats.keys():
                timesRolling = 3
            else:
                timesRolling = 2
        else:
            timesRolling = 1

        critChance = round(1 - pow(0.95, timesRolling), 5)

        ret = {"AC": []}
        for attack in self.combat["Attacks"]:
            toHit = attack["toHit"]["value"]
            avgCritDamage = attack["bonusCritDamage"]
            damage = attack["averageDamage"]
            ret[attack["name"]] = []
            for targetAC in range(toHit + 1, toHit + 22):
                chancePerRoll = round(((21 - (targetAC - toHit)) / 20), 2)
                hitChance = round(1 - pow(1 - chancePerRoll, timesRolling), 5)

                if hitChance >= 1:
                    hitChance = 1

                # if 1 - chancePerRoll <= 0:
                #     normalDamage = (0.05 * damage) + avgCritDamage
                # else:
                normalDamage = (hitChance * damage) + (avgCritDamage * critChance)

                if not targetAC in ret["AC"]:
                    ret["AC"].append(targetAC)

                ret[attack["name"]].append(round(normalDamage, 3))

        return ret

    def getEquipment(self):
        for item in self.equipment:
            self.equipment[item]["displayName"] = "| " + self.equipment[item]["name"]

        return self.equipment

    def getFeatures(self):
        ret = {}

        features = {}
        for cls in self.charClass:
            features[cls.name] = cls.features

        ret["Class"] = features
        ret["Race"] = self.race.getFeatures()
        ret["Misc."] = self.getMiscFeatures()

        return ret

    def cleanProficiencies(self):
        ret = {}
        for item, value in self.proficiencies.items():
            if item == "Armor" or item == "Weapons":
                ret[item] = value
            else:
                ret[item] = sorted(value)

        return ret

    def getFeatsInJSON(self):
        ret = []

        for feat in self.feats:
            ret = ret + [self.feats[feat].toJSON()]

        return ret

    def decodeStats(self):
        stats = self.baseStats
        return stats.split(",")

    def convertEnum(self, enum):
        index = Ability[enum].value
        return Ability(index).name

    def addWeapon(self, weapon):
        self.weapon.append(weapon)
