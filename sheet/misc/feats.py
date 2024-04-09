from sheet.modifiers import Modifier


class Feat:
    source = ""

    def setOptions(self, options):
        self.options = options

    def setSource(self, source):
        self.source = source

    def getModifiers(self, modList):
        return

    def getSpells(self):
        return

    def toJSON(self):
        ret = {"name": self.name, "text": self.text}
        return ret


class ASI(Feat):
    name = "ASI"
    text = []

    def getModifiers(self, modList):
        for stat in iter(self.options["ASI"]):
            i = 0

        if not hasattr(self, "options") or not self.options["ASI"]:
            raise Exception("No ASI specified for the ASI feat")

        stat = next(iter(self.options["ASI"]))

        modList.addModifier(
            Modifier(int(self.options["ASI"][stat]), stat, "ASI:" + self.source)
        )


class ElvenAccuracy(Feat):
    name = "Elven Accuracy"
    text = [
        {
            "type": "normal",
            "text": "Whenever you have advantage on an attack roll using Dexterity, Intelligence, Wisdom, or Charisma, you can reroll one of the dice once.",
        }
    ]

    def getModifiers(self, modList):
        validOptions = ["Dexterity", "Intelligence", "Wisdom", "Charisma"]
        if not hasattr(self, "options") or not self.options["ASI"]:
            raise Exception("No ASI specified for the Elven Accuracy feat")

        stat = next(iter(self.options["ASI"]))
        if not stat in validOptions:
            raise Exception(
                "{} is not a valid ASI choice for Elven Accuracy".format(
                    self.options["ASI"]
                )
            )

        modList.addModifier(
            Modifier(int(self.options["ASI"][stat]), stat, "Elven Accuracy")
        )


class Sharpshooter(Feat):
    name = "Sharpshooter"
    text = [
        {
            "type": "normal",
            "text": """
        Attacking at long range doesn't impose disadvantage on your ranged weapon attack rolls.

        Your ranged weapon attacks ignore half and three-quarters cover.

        Before you make an attack with a ranged weapon that you are proficient with, you can choose to take a -5 penalty to the attack roll. If that attack hits, you add +10 to the attack's damage.
        """,
        }
    ]


class RitualCaster(Feat):
    name = "Ritual Caster"

    def setOptions(self, options):
        super().setOptions(options)

        choice = self.options["class"]

        if choice in ["Wizard"]:
            self.ability = "Intelligence"

        elif choice in ["Bard", "Sorcerer", "Warlock"]:
            self.ability = "Charisma"

        elif choice in ["Cleric", "Druid"]:
            self.ability = "Wisdom"

        else:
            raise Exception(
                "{} is not a valid clas choice for Ritual Caster".format(choice)
            )

        text = """
        You have learned a number of spells that you can cast as rituals. These spells are written in a ritual book, which you must have in hand while casting one of them.

        When you choose this feat, you acquire a ritual book holding two 1st-level spells of your choice. You must choose your spells from the {} spell list, and the spells you choose must have the ritual tag. Your spellcasting ability is {}

        If you come across a spell in written form, such as a magical spell scroll or a wizard's spellbook, you might be able to add it to your ritual book. The spell must be on the {} spell list, the spell's level can be no higher than half your level (rounded up), and it must have the ritual tag. The process of copying the spell into your ritual book takes 2 hours per level of the spell, and costs 50 gp per level. The cost represents the material components you expend as you experiment with the spell to master it, as well as the fine inks you need to record it
        """

        text = text.format(choice, self.ability, choice)

        self.text = [{"type": "normal", "text": text}]

    def getSpells(self, character):
        stats = character.abilityMod
        profBonus = character.profBonus
        modList = character.modList

        abilityMod = stats[self.ability]

        ret = {}
        ret["name"] = "Ritual Caster"
        ret["ability"] = self.ability
        ret["abilityMod"] = abilityMod

        bonus, source = modList.applyModifier("SpellSaveDC")
        source["Base"] = 8
        source["Prof."] = profBonus
        source[self.ability] = abilityMod
        source = {
            k: v
            for k, v in sorted(source.items(), reverse=True, key=lambda item: item[1])
        }
        ret["saveDC"] = {"value": 8 + abilityMod + profBonus + bonus, "source": source}

        bonus, source = modList.applyModifier("SpellAttack")
        source["Prof."] = profBonus
        source[self.ability] = abilityMod
        source = {
            k: v
            for k, v in sorted(source.items(), reverse=True, key=lambda item: item[1])
        }
        ret["spellAttack"] = {"value": profBonus + abilityMod, "source": source}

        ret["spells"] = {}
        ret["spells"]["1"] = {}
        ret["spells"]["1"]["list"] = {
            "Unseen Servant": {"description": ""},
            "Detect Magic": {"description": ""},
        }

        # ret['level']['2'] = {}
        # ret['level']['2']['list'] = {
        # }

        return ret


fifthEditionFeats = {}
fifthEditionFeats["ASI"] = ASI
fifthEditionFeats["Elven Accuracy"] = ElvenAccuracy
fifthEditionFeats["Sharpshooter"] = Sharpshooter
fifthEditionFeats["Ritual Caster"] = RitualCaster


class TwoWeaponFighting(Feat):
    name = "Two-Weapon Fighting"
    text = [
        {"type": "heading", "text": "Benefit:"},
        {
            "type": "normal",
            "text": "Your penalties on attack rolls for fighting with two weapons are reduced. The penalty for your primary hand lessens by 2 and the one for your off hand lessens by 6.",
        },
        {"type": "heading", "text": "Normal:"},
        {
            "type": "normal",
            "text": "If you wield a second weapon in your off hand, you can get one extra attack per round with that weapon. When fighting in this way you suffer a –6 penalty with your regular attack or attacks with your primary hand and a –10 penalty to the attack with your off hand. If your off-hand weapon is light, the penalties are reduced by 2 each. An unarmed strike is always considered light.",
        },
    ]


class ButterflySting(Feat):
    name = "Butterfly Sting"
    text = [
        {
            "type": "normal",
            "text": "When you confirm a critical hit against a creature, you can choose to forgo the effect of the critical hit and grant a critical hit to the next ally who hits the creature with a melee attack before the start of your next turn. Your attack only deals normal damage, and the next ally automatically confirms the hit as a critical.",
        }
    ]


class CombatReflexes(Feat):
    name = "Combat Reflexes"
    text = [
        {"type": "heading", "text": "Benefit:"},
        {
            "type": "normal",
            "text": "You may make a number of additional attacks of opportunity per round equal to your Dexterity bonus. With this feat, you may also make attacks of opportunity while flat-footed.",
        },
        {"type": "heading", "text": "Normal"},
        {
            "type": "normal",
            "text": "A character without this feat can make only one attack of opportunity per round and can’t make attacks of opportunity while flat-footed.",
        },
    ]


pathfinderFeats = {}
pathfinderFeats["Two-Weapon Fighting"] = TwoWeaponFighting
pathfinderFeats["Butterfly Sting"] = ButterflySting
pathfinderFeats["Combat Reflexes"] = CombatReflexes
