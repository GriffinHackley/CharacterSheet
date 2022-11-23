from .classes import Class
from ..modifiers import Modifier, ModifierList

class Wizard(Class):
    proficiencies = {'skills': ['Arcana', 'Investigation', 'Performance'], 'languages':[], 'armor': ['Light'], 'weapons':['Daggers', 'Darts', 'Slings', 'Quarterstaffs', 'Light Crossbows', 'Rapiers'], 'tools':[], 'savingThrows':['Intelligence', 'Wisdom']}
    expertise = {'skills': []}

    def __init__(self, level):
        super().__init__(level, name="Wizard", hitDie='6', edition="5e")
    
    def appendModifiers(self, modList: ModifierList):
        super().appendModifiers(modList)

        modList.addModifier(Modifier(2,"untyped", 'ToHit-Ranged', 'Archery Fighting Style'))

    def getClassFeatures(self):
        ret = {}

        spellcasting = [
            {"type": "normal", "text":"As a student of arcane magic, you have a spellbook containing spells that show the first glimmerings of your true power. See Spells Rules for the general rules of spellcasting and the Spells Listing for the wizard spell list."},

            {"type": "heading", "text":"Cantrips"},
            {"type": "normal", "text":"At 1st level, you know three cantrips of your choice from the wizard spell list. You learn additional wizard cantrips of your choice at higher levels, as shown in the Cantrips Known column of the Wizard table."},

            {"type": "heading", "text":"Spellbook"},
            {"type": "normal", "text":"At 1st level, you have a spellbook containing six 1st-level wizard spells of your choice. Your spellbook is the repository of the wizard spells you know, except your cantrips, which are fixed in your mind."},

            {"type": "heading", "text":"Preparing and Casting Spells"},
            {"type": "normal", "text":"""
                The Wizard table shows how many spell slots you have to cast your wizard spells of 1st level and higher. To cast one of these spells, you must expend a slot of the spell’s level or higher. You regain all expended spell slots when you finish a long rest.

                You prepare the list of wizard spells that are available for you to cast. To do so, choose a number of wizard spells from your spellbook equal to your Intelligence modifier + your wizard level (minimum of one spell). The spells must be of a level for which you have spell slots.

                For example, if you’re a 3rd-level wizard, you have four 1st-level and two 2nd-level spell slots. With an Intelligence of 16, your list of prepared spells can include six spells of 1st or 2nd level, in any combination, chosen from your spellbook. If you prepare the 1st-level spell magic missile, you can cast it using a 1st-level or a 2nd-level slot. Casting the spell doesn’t remove it from your list of prepared spells.

                You can change your list of prepared spells when you finish a long rest. Preparing a new list of wizard spells requires time spent studying your spellbook and memorizing the incantations and gestures you must make to cast the spell: at least 1 minute per spell level for each spell on your list.
            """},

            {"type": "heading", "text":"Spellcasting Ability"},
            {"type": "normal", "text":"""
                Intelligence is your spellcasting ability for your wizard spells, since you learn your spells through dedicated study and memorization. You use your Intelligence whenever a spell refers to your spellcasting ability. In addition, you use your Intelligence modifier when setting the saving throw DC for a wizard spell you cast and when making an attack roll with one.

                Spell save DC = 8 + your proficiency bonus + your Intelligence modifier

                Spell attack modifier = your proficiency bonus + your Intelligence modifier
            """},

            {"type": "heading", "text":"Ritual Casting"},
            {"type": "normal", "text":"You can cast a wizard spell as a ritual if that spell has the ritual tag and you have the spell in your spellbook. You don’t need to have the spell prepared."},

            {"type": "heading", "text":"Spellcasting Focus"},
            {"type": "normal", "text":"You can use an arcane focus (see the Adventuring Gear section) as a spellcasting focus for your wizard spells."},

            {"type": "heading", "text":"Learning Spells of 1st Level and Higher"},
            {"type": "normal", "text":"Each time you gain a wizard level, you can add two wizard spells of your choice to your spellbook for free. Each of these spells must be of a level for which you have spell slots, as shown on the Wizard table. On your adventures, you might find other spells that you can add to your spellbook (see the “Your Spellbook” sidebar)."},
        ]

        arcaneRecovery = [
            {"type": "normal", "text":"You have learned to regain some of your magical energy by studying your spellbook. Once per day when you finish a short rest, you can choose expended spell slots to recover. The spell slots can have a combined level that is equal to or less than half your wizard level (rounded up), and none of the slots can be 6th level or higher."}
        ]

        trainingInWarAndSong = [
            {"type": "normal", "text":"""
                When you adopt this tradition at 2nd level, you gain proficiency with light armor, and you gain proficiency with rapiers.

                You also gain proficiency in the Performance skill if you don’t already have it.
            """}
        ]

        bladesong = [
            {"type": "normal", "text":"""
                Starting at 2nd level, you can invoke an elven magic called the Bladesong, provided that you aren’t wearing medium or heavy armor or using a shield. It graces you with supernatural speed, agility, and focus.

                You can use a bonus action to start the Bladesong, which lasts for 1 minute. It ends early if you are incapacitated, if you don medium or heavy armor or a shield, or if you use two hands to make an attack with a weapon. You can also dismiss the Bladesong at any time (no action required).

                While your Bladesong is active, you gain the following benefits:

                    You gain a bonus to your AC equal to your Intelligence modifier (minimum of +1)

                    Your walking speed increases by 10 feet.

                    You have advantage on Dexterity (Acrobatics) checks.

                    You gain a bonus to any Constitution saving throw you make to maintain your concentration on a spell. The bonus equals your Intelligence modifier (minimum of +1).

                You can use this feature a number of times equal to your proficiency bonus, and you regain all expended uses of it when you finish a long rest.
            """}
        ]

        extraAttack = [
            {"type": "normal", "text":"Starting at 6th level, you can attack twice, instead of once, whenever you take the Attack action on your turn. Moreover, you can cast one of your cantrips in place of one of those attacks."}
        ]

        songOfDefense= [
            {"type": "normal", "text":"Beginning at 10th level, you can direct your magic to absorb damage while your Bladesong is active. When you take damage, you can use your reaction to expend one spell slot and reduce that damage to you by an amount equal to five times the spell slot's level."}
        ]

        songOfVictory= [
            {"type": "normal", "text":"Starting at 14th level, you can add your Intelligence modifier (minimum of +1) to the damage of your melee weapon attacks while your Bladesong is active."}
        ]

        spellMastery = [
            {"type": "normal", "text":"""
                At 18th level, you have achieved such mastery over certain spells that you can cast them at will. Choose a 1st-level wizard spell and a 2nd-level wizard spell that are in your spellbook. You can cast those spells at their lowest level without expending a spell slot when you have them prepared. If you want to cast either spell at a higher level, you must expend a spell slot as normal.

                By spending 8 hours in study, you can exchange one or both of the spells you chose for different spells of the same levels.
            """}
        ]

        signatureSpells= [
            {"type": "normal", "text":"""
                When you reach 20th level, you gain mastery over two powerful spells and can cast them with little effort. Choose two 3rd-level wizard spells in your spellbook as your signature spells. You always have these spells prepared, they don’t count against the number of spells you have prepared, and you can cast each of them once at 3rd level without expending a spell slot. When you do so, you can’t do so again until you finish a short or long rest.

                If you want to cast either spell at a higher level, you must expend a spell slot as normal.
            """}
        ]

        ret['Spellcasting'] = spellcasting
        ret['Arcane Recovery'] = arcaneRecovery 

        if self.level >= 2:
            ret['Training in War and Song'] = trainingInWarAndSong
            ret['Bladesong'] = bladesong

        if self.level >= 3:
            pass

        if self.level >= 4:
            pass

        if self.level >= 5:
            pass

        if self.level >= 6:
            ret['Extra Attack'] = extraAttack

        if self.level >= 7:
            pass

        if self.level >= 8:
            pass

        if self.level >= 9:
            pass

        if self.level >= 10:
            ret['Song of Defense'] = songOfDefense

        if self.level >= 11:
            pass

        if self.level >= 12:
            pass

        if self.level >= 13:
            pass

        if self.level >= 14:
            ret['Song of Victory'] = songOfVictory

        if self.level >= 15:
            pass

        if self.level >= 16:
            pass

        if self.level >= 17:
            pass
        
        if self.level >= 18:
            ret['Spell Mastery'] = spellMastery

        if self.level >= 19:
            pass

        if self.level >= 20:
            ret['Signature Spells'] = signatureSpells
        
        return ret

    def getConsumables(self, stats, proficiencyBonus):
        ret = {}

        ret['Arcane Recovery'] = 1
        ret['Bladesong'] = proficiencyBonus

        return ret
    
    def getSpells(self, stats, profBonus, modList):
        ret = {}
        ability    = "Intelligence"
        abilityMod = stats[ability]

        ret['ability']    = ability
        ret['abilityMod'] = abilityMod


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
        ret['level']['Cantrip'] = {}
        ret['level']['1'] = {}
        ret['level']['2'] = {}

        ret['level']['1']['slots'] = 4
        ret['level']['2']['slots'] = 2


        ret['level']['Cantrip']['list'] = {
            "Booming Blade"   : {"source":"Wizard: Spellcasting"    , "timesPrepared":"-1", "description":""},
            "Mage Hand"       : {"source":"Wizard: Spellcasting"    , "timesPrepared":"-1", "description":""},
            "Mind Sliver"     : {"source":"Wizard: Spellcasting"    , "timesPrepared":"-1", "description":""},
        }

        ret['level']['1']['list'] = {
            "Absorb Elements"   : {"source":"Wizard: Spellcasting"    , "timesPrepared":"1" , "description":""},
            "Detect Magic"      : {"source":"Wizard: Spellcasting"    , "timesPrepared":"-1", "description":""},
            "Feather Fall"      : {"source":"Wizard: Spellcasting"    , "timesPrepared":"1" , "description":""},
            "Find Familiar"     : {"source":"Wizard: Spellcasting"    , "timesPrepared":"-1", "description":""},
            "Identify"          : {"source":"Wizard: Spellcasting"    , "timesPrepared":"-1", "description":""},
            "Jump"              : {"source":"Wizard: Spellcasting"    , "timesPrepared":"1" , "description":""},
            "Shield"            : {"source":"Wizard: Spellcasting"    , "timesPrepared":"1" , "description":""},
            "Silvery Barbs"     : {"source":"Wizard: Spellcasting"    , "timesPrepared":"1" , "description":""},
        }

        ret['level']['2']['list'] = {
            "Invisibility"   : {"source":"Wizard: Spellcasting"    , "timesPrepared":"-1", "description":""},
            "Shadow Blade"   : {"source":"Wizard: Spellcasting"    , "timesPrepared":"-1", "description":""},
        }

        return ret
