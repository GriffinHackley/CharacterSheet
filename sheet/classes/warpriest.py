import math
from .classes import Class
from ..modifiers import Modifier, ModifierList


class Warpriest(Class):
    skillPerLevel = 2
    sacredWeapon = ""
    proficiencies = {
        "armor": ["Light", "Medium", "Heavy", "Shields (except tower shields)"],
        "weapons": ["Simple", "Martial"],
        "languages": [],
    }
    classSkills = [
        "Climb",
        "Craft",
        "Diplomacy",
        "Handle Animal",
        "Heal",
        "Intimidate",
        "Knowledge (Engineering)",
        "Knowledge (Religion)",
        "Profession",
        "Ride",
        "Sense Motive",
        "Spellcraft",
        "Survival",
        "Swim",
    ]

    def __init__(self, level, options):
        self.options = options
        super().__init__(
            level,
            "Warpriest",
            hitDie="8",
            edition="Pathfinder",
            bab="3/4",
            fort="good",
            refl="poor",
            will="good",
        )
        self.sacredWeapon = self.getSacredWeapon()

    def appendModifiers(self, modList: ModifierList):
        super().appendModifiers(modList)

        modList.addModifier(
            Modifier(1, "untyped", "ToHit-Kukri", "Weapon Focus (Kukri)")
        )

    def getClassFeatures(self):
        ret = {}

        spellcasting = [
            {
                "type": "normal",
                "text": """
A warpriest casts divine spells drawn from the cleric spell list. His alignment, however, can restrict him from casting certain spells opposed to his moral or ethical beliefs; see the Chaotic, Evil, Good, and Lawful Spells section. A warpriest must choose and prepare his spells in advance.

A warpriest’s highest level of spells is 6th. Cleric spells of 7th level and above are not on the warpriest class spell list, and a warpriest cannot use spell completion or spell trigger magic items (without making a successful Use Magic Device check) of cleric spells of 7th level or higher.

To prepare or cast a spell, a warpriest must have a Wisdom score equal to at least 10 + the spell’s level. The saving throw DC against a warpriest’s spell is 10 + the spell’s level + the warpriest’s Wisdom modifier.

Like other spellcasters, a warpriest can cast only a certain number of spells of each spell level per day. His base daily spell allotment is given on Table Warpriest. In addition, he receives bonus spells per day if he had a high Wisdom score.

Warpriests meditate or pray for their spells. Each warpriest must choose a time when he must spend 1 hour each day in quiet contemplation or supplication to regain his daily allotment of spells. A warpriest can prepare and cast any spell on the cleric spell list, provided that he can cast spells of that level, but he must choose which spells to prepare during his daily meditation.
""",
            },
            {"type": "heading", "text": "Orisons:"},
            {
                "type": "normal",
                "text": """
Warpriests can prepare a number of orisons, or 0-level spells, each day as noted on Table Warpriest. These spells are cast as any other spell, but aren’t expended when cast and can be used again.
""",
            },
            {"type": "heading", "text": "Spontaneous Casting:"},
            {
                "type": "normal",
                "text": """
A good warpriest (or a neutral warpriest of a good deity) can channel stored spell energy into healing spells that he did not prepare ahead of time. The warpriest can expend any prepared spell that isn’t an orison to cast any cure spell of the same spell level or lower. A cure spell is any spell with “cure” in its name.

A warpriest that is neither good nor evil and whose deity is neither good nor evil chooses whether he can convert spells into either cure spells or inflict spells. Once this choice is made, it cannot be changed. This choice also determines whether the warpriest channels positive or negative energy (see Channel Energy, below).
""",
            },
            {"type": "heading", "text": "Chaotic, Evil, Good, and Lawful Spells:"},
            {
                "type": "normal",
                "text": """
A warpriest cannot cast spells of an alignment opposed to his own or his deity’s (if he has a deity). Spells associated with particular alignments are indicated by the chaotic, evil, good, and lawful descriptors in their spell descriptions.
""",
            },
        ]

        aura = [
            {
                "type": "normal",
                "text": """
A warpriest of a chaotic, evil, good, or lawful deity has a particularly powerful aura (as a cleric) corresponding to the deity’s alignment (see detect evil).
""",
            }
        ]

        blessings = [
            {
                "type": "normal",
                "text": """
A warpriest’s deity influences his alignment, what magic he can perform, his values, and how others see him. Each warpriest can select two blessings from among those granted by his deity (each deity grants the blessings tied to its domains). A warpriest can select an alignment blessing (Chaos, Evil, Good, or Law) only if his alignment matches that domain. If a warpriest isn’t devoted to a particular deity, he still selects two blessings to represent his spiritual inclinations and abilities, subject to GM approval. The restriction on alignment domains still applies.

Each blessing grants a minor power at 1st level and a major power at 10th level. A warpriest can call upon the power of his blessings a number of times per day (in any combination) equal to 3 + 1/2 his warpriest level (to a maximum of 13 times per day at 20th level). Each time he calls upon any one of his blessings, it counts against his daily limit. The save DC for these blessings is equal to 10 + 1/2 the warpriest’s level + the warpriest’s Wisdom modifier.

If a warpriest also has levels in a class that grants cleric domains, the blessings chosen must match the domains selected by that class. Subject to GM discretion, the warpriest can change his former blessings or domains to make them conform.
""",
            }
        ]

        sacredWeapon = [
            {
                "type": "normal",
                "text": """
At 1st level, weapons wielded by a warpriest are charged with the power of his faith. In addition to the favored weapon of his deity, the warpriest can designate a weapon as a sacred weapon by selecting that weapon with the Weapon Focus feat; if he has multiple Weapon Focus feats, this ability applies to all of them. Whenever the warpriest hits with his sacred weapon, the weapon damage is based on his level and not the weapon type. The damage for Medium warpriests is listed on Table 1–14; see the table below for Small and Large warpriests. The warpriest can decide to use the weapon’s base damage instead of the sacred weapon damage—this must be declared before the attack roll is made. (If the weapon’s base damage exceeds the sacred weapon damage, its damage is unchanged.) This increase in damage does not affect any other aspect of the weapon, and doesn’t apply to alchemical items, bombs, or other weapons that only deal energy damage.

At 4th level, the warpriest gains the ability to enhance one of his sacred weapons with divine power as a swift action. This power grants the weapon a +1 enhancement bonus. For every 4 levels beyond 4th, this bonus increases by 1 (to a maximum of +5 at 20th level). If the warpriest has more than one sacred weapon, he can enhance another on the following round by using another swift action. The warpriest can use this ability a number of rounds per day equal to his warpriest level, but these rounds need not be consecutive.

These bonuses stack with any existing bonuses the weapon might have, to a maximum of +5. The warpriest can enhance a weapon with any of the following weapon special abilities: brilliant energy, defending, disruption, flaming, frost, keen, and shock. In addition, if the warpriest is chaotic, he can add anarchic and vicious. If he is evil, he can add mighty cleaving and unholy. If he is good, he can add ghost touch and holy. If he is lawful, he can add axiomatic and merciful. If he is neutral (with no other alignment components), he can add spell storing and thundering. Adding any of these special abilities replaces an amount of bonus equal to the special ability’s base cost. Duplicate abilities do not stack. The weapon must have at least a +1 enhancement bonus before any other special abilities can be added.

If multiple weapons are enhanced, each one consumes rounds of use individually. The enhancement bonus and special abilities are determined the first time the ability is used each day, and cannot be changed until the next day. These bonuses do not apply if another creature is wielding the weapon, but they continue to be in effect if the weapon otherwise leaves the warpriest’s possession (such as if the weapon is thrown). This ability can be ended as a free action at the start of the warpriest’s turn (that round does not count against the total duration, unless the ability is resumed during the same round). If the warpriest uses this ability on a double weapon, the effects apply to only one end of the weapon.
""",
            }
        ]
        fervor = [
            {
                "type": "normal",
                "text": """
At 2nd level, a warpriest can draw upon the power of his faith to heal wounds or harm foes. He can also use this ability to quickly cast spells that aid in his struggles. This ability can be used a number of times per day equal to 1/2 his warpriest level + his Wisdom modifier. By expending one use of this ability, a good warpriest (or one who worships a good deity) can touch a creature to heal it of 1d6 points of damage, plus an additional 1d6 points of damage for every 3 warpriest levels he possesses above 2nd (to a maximum of 7d6 at 20th level). Using this ability is a standard action (unless the warpriest targets himself, in which case it’s a swift action). Alternatively, the warpriest can use this ability to harm an undead creature, dealing the same amount of damage he would otherwise heal with a melee touch attack. Using fervor in this way is a standard action that provokes an attack of opportunity. Undead do not receive a saving throw against this damage. This counts as positive energy.

An evil warpriest (or one who worships an evil deity) can use this ability to instead deal damage to living creatures with a melee touch attack and heal undead creatures with a touch. This counts as negative energy.

A neutral warpriest who worships a neutral deity (or one who is not devoted to a particular deity) uses this ability as a good warpriest if he chose to spontaneously cast cure spells or as an evil warpriest if he chose to spontaneously cast inflict spells.

As a swift action, a warpriest can expend one use of this ability to cast any one warpriest spell he has prepared with a casting time of 1 round or shorter. When cast in this way, the spell can target only the warpriest, even if it could normally affect other or multiple targets. Spells cast in this way ignore somatic components and do not provoke attacks of opportunity. The warpriest does not need to have a free hand to cast a spell in this way.
""",
            }
        ]
        channelEnergy = [
            {
                "type": "normal",
                "text": """
Starting at 4th level, a warpriest can release a wave of energy by channeling the power of his faith through his holy symbol. This energy can be used to deal or heal damage, depending on the type of energy channeled and the creatures targeted. Using this ability is a standard action that expends two uses of his fervor ability and doesn’t provoke an attack of opportunity. The warpriest must present a holy symbol to use this ability. A good warpriest (or one who worships a good deity) channels positive energy and can choose to heal living creatures or to deal damage to undead creatures. A neutral warpriest who worships a neutral deity (or one who is not devoted to a particular deity) channels positive energy if he chose to spontaneously cast cure spells or negative energy if he chose to spontaneously cast inflict spells.

Channeling energy causes a burst that affects all creatures of one type (either undead or living) in a 30-foot radius centered on the warpriest. The amount of damage dealt or healed is equal to the amount listed in the fervor ability. Creatures that take damage from channeled energy must succeed at a Will saving throw to halve the damage. The save DC is 10 + 1/2 the warpriest’s level + the warpriest’s Wisdom modifier. Creatures healed by channeled energy cannot exceed their maximum hit point total—all excess healing is lost. A warpriest can choose whether or not to include himself in this effect.
""",
            }
        ]
        sacredArmor = [
            {
                "type": "normal",
                "text": """
At 7th level, the warpriest gains the ability to enhance his armor with divine power as a swift action. This power grants the armor a +1 enhancement bonus. For every 3 levels beyond 7th, this bonus increases by 1 (to a maximum of +5 at 19th level). The warpriest can use this ability a number of minutes per day equal to his warpriest level. This duration must be used in 1-minute increments, but they don’t need to be consecutive.

These bonuses stack with any existing bonuses the armor might have, to a maximum of +5. The warpriest can enhance armor any of the following armor special abilities: energy resistance (normal, improved, and greater), fortification (heavy, light, or moderate), glamered, and spell resistance (13, 15, 17, and 19). Adding any of these special abilities replaces an amount of bonus equal to the special ability’s base cost. For this purpose, glamered counts as a +1 bonus, energy resistance counts as +2, improved energy resistance counts as +4, and greater energy resistance counts as +5. Duplicate abilities do not stack. The armor must have at least a +1 enhancement bonus before any other special abilities can be added.

The enhancement bonus and armor special abilities are determined the first time the ability is used each day and cannot be changed until the next day. These bonuses apply only while the warpriest is wearing the armor, and end immediately if the armor is removed or leaves the warpriest’s possession. This ability can be ended as a free action at the start of the warpriest’s turn. This ability cannot be applied to a shield.

When the warpriest uses this ability, he can also use his sacred weapon ability as a free action by expending one use of his fervor.
""",
            }
        ]
        aspectOfWar = [
            {
                "type": "normal",
                "text": """
At 20th level, the warpriest can channel an aspect of war, growing in power and martial ability. Once per day as a swift action, a warpriest can treat his level as his base attack bonus, gains DR 10/—, and can move at his full speed regardless of the armor he is wearing or his encumbrance. In addition, the blessings he calls upon don’t count against his daily limit during this time. This ability lasts for 1 minute.
""",
            }
        ]

        ret["Aura"] = aura
        ret["Blessings"] = blessings
        ret["Sacred Weapon"] = sacredWeapon
        ret["Spellcasting"] = spellcasting

        if self.level >= 2:
            ret["Fervor"] = fervor

        if self.level >= 3:
            pass

        if self.level >= 4:
            ret["Channel Energy"] = channelEnergy

        if self.level >= 5:
            pass

        if self.level >= 6:
            pass

        if self.level >= 7:
            ret["Sacred Armor"] = sacredArmor

        if self.level >= 8:
            pass

        if self.level >= 9:
            pass

        if self.level >= 10:
            pass

        if self.level >= 11:
            pass

        if self.level >= 12:
            pass

        if self.level >= 13:
            pass

        if self.level >= 14:
            pass

        if self.level >= 15:
            pass

        if self.level >= 16:
            pass

        if self.level >= 17:
            pass

        if self.level >= 18:
            pass

        if self.level >= 19:
            pass

        if self.level >= 20:
            ret["Aspect of War"] = aspectOfWar

        return ret

    def getSacredWeapon(self):
        ret = {}

        ret["damageDie"] = "1d6"
        ret["totalEnhance"] = 1

        return ret

    def getConsumables(self, stats, profBonus):
        ret = []
        ret.append({"name": "Blessings", "number": 3 + math.floor(stats["Wisdom"] / 2)})

        if self.level >= 2:
            ret.append({"name": "Fervor", "number": 3 + math.floor(self.level / 2)})

        if self.level >= 4:
            ret.append({"name": "Focus Weapon", "number": self.level})

        return ret

    def getSpells(self, stats, modList):
        ret = {}
        ability = "Wisdom"
        abilityMod = stats[ability]

        ret["ability"] = ability
        ret["abilityMod"] = abilityMod
        ret["castingType"] = ["known", "ritual"]

        bonus, source = modList.applyModifier("SpellSaveDC")
        source["Base"] = 10
        source[ability] = abilityMod
        source = {
            k: v
            for k, v in sorted(source.items(), reverse=True, key=lambda item: item[1])
        }
        ret["saveDC"] = {"value": 10 + abilityMod + bonus, "source": source}

        ret["spells"] = {}
        ret["spells"]["Cantrip"] = {}
        ret["spells"]["1"] = {}
        ret["spells"]["2"] = {}

        ret["spells"]["1"]["slots"] = 3
        ret["spells"]["2"]["slots"] = 1

        # TODO: Implement this better
        # Get bonus spells from ability score
        ret["spells"]["1"]["slots"] = ret["spells"]["1"]["slots"] + 1
        ret["spells"]["2"]["slots"] = ret["spells"]["2"]["slots"] + 1

        ret["spells"]["Cantrip"]["list"] = {
            "Create Water": {
                "source": "Warpriest: Spellcasting",
                "timesPrepared": -1,
                "description": "",
            },
            "Detect Magic": {
                "source": "Warpriest: Spellcasting",
                "timesPrepared": -1,
                "description": "",
            },
            "Guidance": {
                "source": "Warpriest: Spellcasting",
                "timesPrepared": -1,
                "description": "",
            },
            "Read Magic": {
                "source": "Warpriest: Spellcasting",
                "timesPrepared": -1,
                "description": "",
            },
        }
        ret["spells"]["1"]["list"] = {
            "Divine Favor": {
                "source": "Warpriest: Spellcasting",
                "timesPrepared": 2,
                "description": "",
            },
            "Shield of Faith": {
                "source": "Warpriest: Spellcasting",
                "timesPrepared": 1,
                "description": "",
            },
            "Unprepared": {
                "source": "Warpriest: Spellcasting",
                "timesPrepared": 1,
                "description": "",
            },
        }
        ret["spells"]["2"]["list"] = {
            "Cats Grace": {
                "source": "Warpriest: Spellcasting",
                "timesPrepared": 1,
                "description": "",
            },
            "Ironskin": {
                "source": "Warpriest: Spellcasting",
                "timesPrepared": 1,
                "description": "",
            },
        }

        return ret
