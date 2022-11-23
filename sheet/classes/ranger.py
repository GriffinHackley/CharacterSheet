from .classes import Class
from ..modifiers import Modifier, ModifierList

class Ranger(Class):
    proficiencies = {'skills': ['Insight', 'Stealth', 'Survival'], 'languages':['Draconic', 'Sylvan'], 'armor': ['Light', 'Medium'], 'weapons':['Simple', 'Martial'], 'tools':[], 'savingThrows':['Strength', 'Dexterity']}
    expertise = {'skills': ['Stealth']}

    def __init__(self, level):
        super().__init__(level, name="Ranger", hitDie='10', edition="5e")

    def appendModifiers(self, modList: ModifierList):
        super().appendModifiers(modList)

        modList.addModifier(Modifier(2,"untyped", 'ToHit-Ranged', 'Archery Fighting Style'))
        modList.addModifier(Modifier('Wisdom',"untyped", 'Initiative', 'Dread Ambusher'))

    def getClassFeatures(self):
        ret = {}

        favoredFoe = [
{"type": "normal", "text":"""
When you hit a creature with an attack roll, you can call on your mystical bond with nature to mark the target as your favored enemy for 1 minute or until you lose your concentration (as if you were concentrating on a spell).

The first time on each of your turns that you hit the favored enemy and deal damage to it, including when you mark it, you increase that damage by 1d4.

You can use this feature to mark a favored enemy a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.

This feature's extra damage increases when you reach certain levels in this class: to 1d6 at 6th level and to 1d8 at 14th level.
"""}]

        deftExplorer = [
{"type": "normal", "text":"""
You are an unsurpassed explorer and survivor, both in the wilderness and in dealing with others on your travels. You gain the Canny benefit below, and you gain an additional benefit when you reach 6th level and 10th level in this class.
"""}, 

{"type": "heading", "text":"Canny:"},
{"type": "normal", "text":"""
Your proficiency bonus is doubled for any ability check you make using stealth.

You can also speak, read, and write Draconic and Sylvan
"""}]

        if self.level >= 6:
            deftExplorer.append(
{"type": "heading", "text":"Roving:"})
            deftExplorer.append(
{"type": "normal", "text":"""
Your walking speed increases by 5, and you gain a climbing speed and a swimming speed equal to your walking speed.
"""})
        if self.level >= 10:
            deftExplorer.append(
{"type": "heading", "text":"Tireless:"})

            deftExplorer.append(
{"type": "normal", "text":"""
As an action, you can give yourself a number of temporary hit points equal to 1d8 + your Wisdom modifier (minimum of 1 temporary hit point). You can use this action a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.

In addition, whenever you finish a short rest, your exhaustion level, if any, is decreased by 1.
"""})

        fightingStyle = [
{"type": "normal", "text":"""
At 2nd level, you adopt a particular style of fighting as your specialty. You can't take a Fighting Style option more than once, even if you later get to choose again.
"""},

{"type": "heading", "text":"Archery:"},
{"type": "normal", "text":"""
You gain a +2 bonus to attack rolls you make with ranged weapons.
"""}]

        spellcasting = [
{"type": "normal", "text":"""
By the time you reach 2nd level, you have learned to use the magical essence of nature to cast spells, much as a druid does.
"""},

{"type": "heading", "text":"Spell Slots"},
{"type": "normal", "text":"""
The Ranger table shows how many spell slots you have to cast your ranger spells of 1st level and higher. To cast one of these spells, you must expend a slot of the spell's level or higher. You regain all expended spell slots when you finish a long rest.

For example, if you know the 1st-level spell Animal Friendship and have a 1st-level and a 2nd-level spell slot available, you can cast Animal Friendship using either slot.
"""},

{"type": "heading", "text":"Spells Known of 1st Level and Higher"},
{"type": "normal", "text":"""
You know two 1st-level spells of your choice from the ranger spell list.

The Spells Known column of the Ranger table shows when you learn more ranger spells of your choice. Each of these spells must be of a level for which you have spell slots. For instance, when you reach 5th level in this class, you can learn one new spell of 1st or 2nd level.

Additionally, when you gain a level in this class, you can choose one of the ranger spells you know and replace it with another spell from the ranger spell list, which also must be of a level for which you have spell slots.
"""},

{"type": "heading", "text":"Spellcasting Ability"},
{"type": "normal", "text":"""
Wisdom is your spellcasting ability for your ranger spells, since your magic draws on your attunement to nature. You use your Wisdom whenever a spell refers to your spellcasting ability. In addition, you use your Wisdom modifier when setting the saving throw DC for a ranger spell you cast and when making an attack roll with one.

Spell save DC = 8 + your proficiency bonus + your Wisdom modifier

Spell attack modifier = your proficiency bonus + your Wisdom modifier
"""},

{"type": "heading", "text":"Spellcasting Focus"},
{"type": "normal", "text":"""
At 2nd level, you can use a druidic focus as a spellcasting focus for your ranger spells. A druidic focus might be a sprig of mistletoe or holly, a wand or rod made of yew or another special wood, a staff drawn whole from a living tree, or an object incorporating feathers, fur, bones, and teeth from sacred animals.
"""}]

        primalAwareness = [
{"type": "normal", "text":"""
You can focus your awareness through the interconnections of nature: you learn additional spells when you reach certain levels in this class if you don't already know them, as shown in the Primal Awareness Spells table. These spells don't count against the number of ranger spells you know.
"""},

{"type": "table", "text":{
    '3' : "Speak With Animals",
    '5' : "Beast Sense",
    '9' : "Speak With Plants",
    '13': "Locate Creature",
    '17': "Commune With Nature",
}}]

        martialVersatility = [
{"type": "normal", "text":"""
Whenever you reach a level in this class that grants the Ability Score Improvement feature, you can replace a fighting style you know with another fighting style available to rangers. This replacement represents a shift of focus in your martial practice.
"""}]

        extraAttack = [
{"type": "normal", "text":"""
Beginning at 5th level, you can attack twice, instead of once, whenever you take the Attack action on your turn.
"""}]

        landsStride = [
{"type": "normal", "text":"""
Starting at 8th level, moving through nonmagical difficult terrain costs you no extra movement. You can also pass through nonmagical plants without being slowed by them and without taking damage from them if they have thorns, spines, or a similar hazard.

In addition, you have advantage on saving throws against plants that are magically created or manipulated to impede movement, such as those created by the Entangle spell.
"""}]

        naturesVeil = [
{"type": "normal", "text":"""
This 10th-level feature replaces the Hide in Plain Sight feature. You gain no benefit from the replaced feature and don't qualify for anything in the game that requires it.

You draw on the powers of nature to hide yourself from view briefly. As a bonus action, you can magically become invisible, along with any equipment you are wearing or carrying, until the start of your next turn.

You can use this feature a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.
"""}]


        vanish = [
{"type": "normal", "text":"""
Starting at 14th level, you can use the Hide action as a bonus action on your turn. Also, you can't be tracked by nonmagical means, unless you choose to leave a trail.
"""}]

        feralSenses = [
{"type": "normal", "text":"""
At 18th level, you gain preternatural senses that help you fight creatures you can't see. When you attack a creature you can't see, your inability to see it doesn't impose disadvantage on your attack rolls against it.

You are also aware of the location of any invisible creature within 30 feet of you, provided that the creature isn't hidden from you and you aren't blinded or deafened.
"""}]

        foeSlayer = [
{"type": "normal", "text":"""
At 20th level, you become an unparalleled hunter of your enemies. Once on each of your turns, you can add your Wisdom modifier to the attack roll or the damage roll of an attack you make against one of your favored enemies. You can choose to use this feature before or after the roll, but before any effects of the roll are applied.
"""}]

        ret['Favored Foe'] = favoredFoe
        ret['Deft Explorer'] = deftExplorer

        if self.level >= 2:
            ret['Fighting Style'] = fightingStyle
            ret['Spellcasting'] = spellcasting

        if self.level >= 3:
            ret['Primal Awareness'] = primalAwareness

        if self.level >= 4:
            ret['Martial Versatility'] = martialVersatility

        if self.level >= 5:
            ret['Extra Attack'] = extraAttack

        if self.level >= 6:
            pass

        if self.level >= 7:
            pass

        if self.level >= 8:
            ret['Lands Stride'] = landsStride

        if self.level >= 9:
            pass

        if self.level >= 10:
            pass

        if self.level >= 11:
            ret['Natures Veil'] = naturesVeil

        if self.level >= 12:
            pass

        if self.level >= 13:
            pass

        if self.level >= 14:
            ret['Vanish'] = vanish

        if self.level >= 15:
            pass

        if self.level >= 16:
            pass

        if self.level >= 17:
            pass
        
        if self.level >= 18:
            ret['Feral Senses'] = feralSenses

        if self.level >= 19:
            pass

        if self.level >= 20:
            ret['Foe Slayer'] = foeSlayer
        
        return ret

    def getConsumables(self, stats, proficiencyBonus):
        huntersMark = stats['Wisdom']
        favoredFoe = proficiencyBonus
        return {'Favored Foe': favoredFoe, 'Hunters Mark': huntersMark}
    
    def getSpells(self, stats, profBonus, modList):
        ret = {}
        ability    = "Wisdom"
        abilityMod = stats[ability]

        ret['ability']    = ability
        ret['abilityMod'] = abilityMod

        bonus, source = modList.applyModifier("SpellSaveDC")

        bonus, source = modList.applyModifier("SpellSaveDC")
        source['Base'] = 8
        source['Prof.'] = profBonus
        source[ability] = abilityMod
        source = {k: v for k, v in sorted(source.items(), reverse=True, key=lambda item: item[1])}
        ret['saveDC'] = {'value': 8 + abilityMod + profBonus + bonus, 'source':source}

        bonus, source = modList.applyModifier("SpellAttack")
        source['Prof.'] = profBonus
        source[ability] = abilityMod
        source = {k: v for k, v in sorted(source.items(), reverse=True, key=lambda item: item[1])}
        ret['spellAttack'] = {'value':profBonus + abilityMod, 'source':source}

        ret['level'] = {}
        ret['level']['1'] = {}

        ret['level']['1']['slots'] = 3

        ret['level']['1']['list'] = {
            "Absorb Elements"   : {"source":"Ranger: Spellcasting"    , "timesPrepared":"-1", "description":""},
            "Cure Wounds"       : {"source":"Ranger: Spellcasting"    , "timesPrepared":"-1", "description":""},
            "Hunter\'s Mark"    : {"source":"Ranger: Spellcasting"    , "timesPrepared":"-1", "description":""},
            "Disguise Self"     : {"source":"Ranger: Gloom Stalker"   , "timesPrepared":"-1", "description":""},
            "Speak With Animals": {"source":"Ranger: Primal Awareness", "timesPrepared":"-1", "description":""},
        }

        return ret
