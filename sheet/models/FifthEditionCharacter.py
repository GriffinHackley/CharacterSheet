import re
import math

from sheet.misc.spells import SpellList
from ..lists import Ability, skill_list_5e
from ..misc.feats import fifthEditionFeats
from sheet.models.Characters import Character
from rest_framework.exceptions import APIException
from ..misc.backgrounds import FifthEditionBackground


class FifthEditionCharacter(Character):
    def build(self):
        self.skillList = skill_list_5e
        self.proficiencies = {
            "skills": [],
            "languages": [],
            "armor": [],
            "weapons": [],
            "tools": [],
            "savingThrows": [],
        }
        self.expertise = {"skills": [], "tools": []}

        super().build()

    def __init__(self, character):
        super().fromCharacter(character)

    def getHeader(self):
        ret = super().getHeader()
        return ret

    def calculateSaves(self):
        ret = {}

        for ability in Ability:
            ret[ability.name] = {"ability": ability.name, "proficiency": False}
            statBonus = self.abilityMod[ability.name]

            saveName = ability.name + " Saving Throw"
            bonus, source = self.modList.applyModifier(saveName)

            source["Base"] = statBonus

            statBonus += bonus
            if ability.name in self.proficiencies["savingThrows"]:
                ret[ability.name]["proficiency"] = True
                source["Prof."] = self.profBonus
                statBonus += self.profBonus

            source = {
                k: v
                for k, v in sorted(
                    source.items(), reverse=True, key=lambda item: item[1]
                )
            }

            ret[ability.name] = ret[ability.name] | {
                "value": statBonus,
                "source": source,
            }

        return ret

    def calculateToHit(self, weapon):
        # Base to Hit
        totalValue, source = self.modList.applyModifier("ToHit")

        attackStat = weapon["toHitAbility"]
        totalValue += self.abilityMod[attackStat]
        source[attackStat] = self.abilityMod[attackStat]

        totalValue += self.profBonus
        source["Prof."] = self.profBonus

        if "Melee" in weapon["tags"]:
            bonus, source = self.modList.applyModifier("ToHit-Melee")
            totalValue += bonus
            source.update(source)

        if "Ranged" in weapon["tags"]:
            bonus, source = self.modList.applyModifier("ToHit-Ranged")
            totalValue += bonus
            source.update(source)

            # Parse range increments from weapon properties
            reg = re.compile(r"Range\(([0-9]+)\/([0-9]+)\)")
            if any((match := reg.match(item)) for item in weapon["properties"]):
                closeRange = match.group(1)
                maxRange = match.group(2)
                # weaponRet["range"] = closeRange + "/" + maxRange

        return {"value": totalValue, "source": source}

    def calculateDamageMod(self, weapon):
        # Base Damage
        damageMod = 0
        damageMod += weapon["bonus"]
        bonus, source = self.modList.applyModifier("Damage")
        damageMod += bonus

        if weapon["bonus"] > 0:
            # toHit += weapon["bonus"]
            # toHitSource["Enchant"] = weapon["bonus"]
            source["Enchant"] = weapon["bonus"]
        damageStat = weapon["damageAbility"]
        if "TWF" in weapon["tags"]:
            if "Main" in weapon["tags"]:
                damageMod += self.abilityMod[damageStat]
                source[damageStat] = self.abilityMod[damageStat]
                name = "Main " + weapon["name"]
            elif "Off-Hand" in weapon["tags"]:
                name = "Off-Hand " + weapon["name"]
            else:
                raise APIException(
                    "The TWF tag was on this weapon but neither the Main or Off-Hand tags were found"
                )
        else:
            damageMod += self.abilityMod[damageStat]
            source[damageStat] = self.abilityMod[damageStat]

        return {"value": damageMod, "source": source}

    def calculateAttacks(self):
        ret = []

        for weapon in self.weapon:
            weaponRet = super().attackInit(weapon)

            weaponRet["toHit"] = self.calculateToHit(weapon)
            weaponRet["damageMod"] = self.calculateDamageMod(weapon)

            weaponRet["name"] = weapon["name"]

            weaponRet = super().calculateAttack(weaponRet, weapon)

            ret.append(weaponRet)

        return ret

    def calculateAC(self):
        bonus, source = self.modList.applyModifier("AC")

        total = 10
        source["Base"] = 10

        total += bonus

        source["Armor"] = self.equipment["armor"]["armorBonus"]
        total += self.equipment["armor"]["armorBonus"]

        ability = self.convertEnum(self.equipment["armor"]["ability"])
        if self.abilityMod[ability] > self.equipment["armor"]["maxAbility"]:
            source["Dex*"] = self.equipment["armor"]["maxAbility"]
            total += self.equipment["armor"]["maxAbility"]
        else:
            source["Dex"] = self.abilityMod[ability]
            total += self.abilityMod[ability]

        source = {
            k: v
            for k, v in sorted(source.items(), reverse=True, key=lambda item: item[1])
        }

        return {"value": total, "source": source}

    def getProfBonus(self):
        totalLevel = 0
        for cls in self.charClass:
            totalLevel += cls.level

        bonus = math.floor(2 + ((totalLevel - 1) / 4))
        return bonus

    def calculateSkills(self):
        ret = []
        list = skill_list_5e

        expertiseList = []
        for cls in self.charClass:
            expertiseList.append(cls.getExpertise())

        for key, value in list.items():
            current = {
                "name": key,
                "isKnowledge": False,
                "proficiency": False,
                "expertise": False,
            }
            statBonus = 0

            ability = self.convertEnum(value["ability"])
            statBonus += self.abilityMod[ability]
            bonus, source = self.modList.applyModifier(key)
            source[ability] = statBonus
            statBonus += bonus

            expertise = False
            if key in expertiseList:
                expertise = True

            if key in self.proficiencies["skills"]:
                current["proficiency"] = True
                source["Prof."] = self.profBonus
                statBonus += self.profBonus
                if expertise:
                    current["expertise"] = True
                    source["Expertise"] = self.profBonus
                    statBonus += self.profBonus
            else:
                bonus, modSource = self.modList.applyModifier(
                    "Non-Proficient Ability Check"
                )
                statBonus += bonus
                if modSource:
                    i = 0
                source = source | modSource
                # source[modSource] = bonus

            current = current | {
                "ability": ability,
                "value": statBonus,
                "source": source,
            }

            ret.append(current)

        return ret

    def applyClass(self):
        super().applyClass()
        self.profBonus = self.getProfBonus()

    def applyBackground(self):
        self.background = FifthEditionBackground(self.background)

        self.proficiencies["skills"] += self.background.skills
        self.proficiencies["tools"] += self.background.tools
        self.proficiencies["languages"] += self.background.languages

    def applyFeats(self):
        return super().applyFeats(fifthEditionFeats)

    def applySpells(self):
        spellList = SpellList("5e")

        hasSpells = False
        for cls in self.charClass:
            if not hasattr(cls, "spellList"):
                continue
            spellList.addClass(cls)
            hasSpells = True

        if hasSpells:
            self.toggles.addToggleList(spellList.getToggles())
            self.spellList = spellList

    def getSpells(self):
        if not self.spellList:
            return None

        ret = []
        headers = {}
        for cls in self.charClass:
            headers[cls.name] = self.spellList.getSpellHeader(
                cls, self.abilityMod, self.profBonus, self.modList, self.saves
            )

        # if "Ritual Caster" in [feat.name for feat in self.feats]:
        #     for feat in self.feats:
        #         ret.append(feat.getSpells(self))

        ret = {
            "slots": self.spellList.getSpellSlots(),
            "list": self.spellList.getSpellList(),
            "headers": headers,
        }

        return ret

    def getMiscFeatures(self):
        ret = {}

        ret["Feats"] = self.getFeatsInJSON()

        ret["Background"] = [
            {
                "name": self.background.feature["name"],
                "text": self.background.feature["feature"],
            }
        ]

        return ret

    def getProficiencies(self):
        ret = []

        ret = ret + ["fdsa"]

        return ret

    def initModifiers(self):
        pass
