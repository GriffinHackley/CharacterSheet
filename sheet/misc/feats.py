from sheet.modifiers import Modifier

def ElvenAccuracy(character):
    character.modList.addModifier(Modifier(1, "untyped", 'Dexterity', 'Elven Accuracy')) 
    return [
        {"type": "normal", "text":"Whenever you have advantage on an attack roll using Dexterity, Intelligence, Wisdom, or Charisma, you can reroll one of the dice once."}
    ]

def Sharpshooter(character):
    return [
        {"type": "normal", "text":"""
        Attacking at long range doesn't impose disadvantage on your ranged weapon attack rolls.

        Your ranged weapon attacks ignore half and three-quarters cover.

        Before you make an attack with a ranged weapon that you are proficient with, you can choose to take a -5 penalty to the attack roll. If that attack hits, you add +10 to the attack's damage.
        """}
    ]

def RitualCaster(character):
    return [
        {"type": "normal", "text":"""
        You have learned a number of spells that you can cast as rituals. These spells are written in a ritual book, which you must have in hand while casting one of them.

        When you choose this feat, you acquire a ritual book holding two 1st-level spells of your choice. Choose one of the following classes: bard, cleric, druid, sorcerer, warlock, or wizard. You must choose your spells from that class's spell list, and the spells you choose must have the ritual tag. The class you choose also must have the ritual tag. The class you choose also determines your spellcasting ability for these spells: Charisma for bard, sorcerer, or warlock; Wisdom for cleric or druid; or Intelligence for wizard.

        If you come across a spell in written form, such as a magical spell scroll or a wizard's spellbook, you might be able to add it to your ritual book. The spell must be on the spell list for the class you chose, the spell's level can be no higher than half your level (rounded up), and it must have the ritual tag. The process of copying the spell into your ritual book takes 2 hours per level of the spell, and costs 50 gp per level. The cost represents the material components you expend as you experiment with the spell to master it, as well as the fine inks you need to record it
        """}
    ]

fifthEditionFeats = {}
fifthEditionFeats['Elven Accuracy'] = ElvenAccuracy
fifthEditionFeats['Sharpshooter'] = Sharpshooter
fifthEditionFeats['Ritual Caster'] = RitualCaster



def TwoWeaponFighting(character):
    return [
        {"type": "heading", "text":"Benefit:"},
        {"type": "normal", "text":"Your penalties on attack rolls for fighting with two weapons are reduced. The penalty for your primary hand lessens by 2 and the one for your off hand lessens by 6."},
        {"type": "heading", "text":"Normal:"},
        {"type": "normal", "text":"If you wield a second weapon in your off hand, you can get one extra attack per round with that weapon. When fighting in this way you suffer a –6 penalty with your regular attack or attacks with your primary hand and a –10 penalty to the attack with your off hand. If your off-hand weapon is light, the penalties are reduced by 2 each. An unarmed strike is always considered light."},
    ]

def ButterflySting(character):
    return [
        {"type": "normal", "text":"When you confirm a critical hit against a creature, you can choose to forgo the effect of the critical hit and grant a critical hit to the next ally who hits the creature with a melee attack before the start of your next turn. Your attack only deals normal damage, and the next ally automatically confirms the hit as a critical."}
    ]

def CombatReflexes(character):
    return [
        {"type": "heading", "text":"Benefit:"},
        {"type": "normal", "text":"You may make a number of additional attacks of opportunity per round equal to your Dexterity bonus. With this feat, you may also make attacks of opportunity while flat-footed."},
        {"type": "heading", "text":"Normal"},
        {"type": "normal", "text":"A character without this feat can make only one attack of opportunity per round and can’t make attacks of opportunity while flat-footed."},
    ]

pathfinderFeats = {}
pathfinderFeats["Two-Weapon Fighting"] = TwoWeaponFighting
pathfinderFeats['Butterfly Sting'] = ButterflySting
pathfinderFeats['Combat Reflexes'] = CombatReflexes