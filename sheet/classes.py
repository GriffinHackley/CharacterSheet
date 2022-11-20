import math
from .modifiers import Modifier, ModifierList

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
    
class Warpiest(Class):    
    skillPerLevel = 2
    sacredWeapon  = ''
    proficiencies = {'armor': ['Light', 'Medium', 'Heavy', 'Shields (except tower shields)'], 'weapons':['Simple', 'Martial'],'languages':[]}
    classSkills   = ['Climb', 'Craft', 'Diplomacy', 'Handle Animal', 'Heal', 'Intimidate', 'Knowledge (Engineering)', 
                     'Knowledge (Religion)', 'Profession', 'Ride', 'Sense Motive', 'Spellcraft', 'Survival', 'Swim']

    def __init__(self, level):
        super().__init__(level, 'Warpriest', hitDie='8', edition="Pathfinder", bab="3/4", fort="good", refl="poor", will="good")
        self.sacredWeapon = self.getSacredWeapon()
    
    def appendModifiers(self, modList: ModifierList):
        super().appendModifiers(modList)

        modList.addModifier(Modifier(1,"untyped", 'ToHit-Kukri', 'Weapon Focus (Kukri)'))
    
    def getClassFeatures(self):
        ret = {}

        spellcasting = [
{"type": "normal", "text":"""
A warpriest casts divine spells drawn from the cleric spell list. His alignment, however, can restrict him from casting certain spells opposed to his moral or ethical beliefs; see the Chaotic, Evil, Good, and Lawful Spells section. A warpriest must choose and prepare his spells in advance.

A warpriest’s highest level of spells is 6th. Cleric spells of 7th level and above are not on the warpriest class spell list, and a warpriest cannot use spell completion or spell trigger magic items (without making a successful Use Magic Device check) of cleric spells of 7th level or higher.

To prepare or cast a spell, a warpriest must have a Wisdom score equal to at least 10 + the spell’s level. The saving throw DC against a warpriest’s spell is 10 + the spell’s level + the warpriest’s Wisdom modifier.

Like other spellcasters, a warpriest can cast only a certain number of spells of each spell level per day. His base daily spell allotment is given on Table Warpriest. In addition, he receives bonus spells per day if he had a high Wisdom score.

Warpriests meditate or pray for their spells. Each warpriest must choose a time when he must spend 1 hour each day in quiet contemplation or supplication to regain his daily allotment of spells. A warpriest can prepare and cast any spell on the cleric spell list, provided that he can cast spells of that level, but he must choose which spells to prepare during his daily meditation.
"""},

{"type": "heading", "text":"Orisons:"},
{"type": "normal", "text":"""
Warpriests can prepare a number of orisons, or 0-level spells, each day as noted on Table Warpriest. These spells are cast as any other spell, but aren’t expended when cast and can be used again.
"""},

{"type": "heading", "text":"Spontaneous Casting:"},
{"type": "normal", "text":"""
A good warpriest (or a neutral warpriest of a good deity) can channel stored spell energy into healing spells that he did not prepare ahead of time. The warpriest can expend any prepared spell that isn’t an orison to cast any cure spell of the same spell level or lower. A cure spell is any spell with “cure” in its name.

A warpriest that is neither good nor evil and whose deity is neither good nor evil chooses whether he can convert spells into either cure spells or inflict spells. Once this choice is made, it cannot be changed. This choice also determines whether the warpriest channels positive or negative energy (see Channel Energy, below).
"""},

{"type": "heading", "text":"Chaotic, Evil, Good, and Lawful Spells:"},
{"type": "normal", "text":"""
A warpriest cannot cast spells of an alignment opposed to his own or his deity’s (if he has a deity). Spells associated with particular alignments are indicated by the chaotic, evil, good, and lawful descriptors in their spell descriptions.
"""}]

        aura = [
{"type": "normal", "text":"""
A warpriest of a chaotic, evil, good, or lawful deity has a particularly powerful aura (as a cleric) corresponding to the deity’s alignment (see detect evil).
"""}]

        blessings = [
{"type": "normal", "text":"""
A warpriest’s deity influences his alignment, what magic he can perform, his values, and how others see him. Each warpriest can select two blessings from among those granted by his deity (each deity grants the blessings tied to its domains). A warpriest can select an alignment blessing (Chaos, Evil, Good, or Law) only if his alignment matches that domain. If a warpriest isn’t devoted to a particular deity, he still selects two blessings to represent his spiritual inclinations and abilities, subject to GM approval. The restriction on alignment domains still applies.

Each blessing grants a minor power at 1st level and a major power at 10th level. A warpriest can call upon the power of his blessings a number of times per day (in any combination) equal to 3 + 1/2 his warpriest level (to a maximum of 13 times per day at 20th level). Each time he calls upon any one of his blessings, it counts against his daily limit. The save DC for these blessings is equal to 10 + 1/2 the warpriest’s level + the warpriest’s Wisdom modifier.

If a warpriest also has levels in a class that grants cleric domains, the blessings chosen must match the domains selected by that class. Subject to GM discretion, the warpriest can change his former blessings or domains to make them conform.
"""}]

        sacredWeapon= [
{"type": "normal", "text":"""
At 1st level, weapons wielded by a warpriest are charged with the power of his faith. In addition to the favored weapon of his deity, the warpriest can designate a weapon as a sacred weapon by selecting that weapon with the Weapon Focus feat; if he has multiple Weapon Focus feats, this ability applies to all of them. Whenever the warpriest hits with his sacred weapon, the weapon damage is based on his level and not the weapon type. The damage for Medium warpriests is listed on Table 1–14; see the table below for Small and Large warpriests. The warpriest can decide to use the weapon’s base damage instead of the sacred weapon damage—this must be declared before the attack roll is made. (If the weapon’s base damage exceeds the sacred weapon damage, its damage is unchanged.) This increase in damage does not affect any other aspect of the weapon, and doesn’t apply to alchemical items, bombs, or other weapons that only deal energy damage.

At 4th level, the warpriest gains the ability to enhance one of his sacred weapons with divine power as a swift action. This power grants the weapon a +1 enhancement bonus. For every 4 levels beyond 4th, this bonus increases by 1 (to a maximum of +5 at 20th level). If the warpriest has more than one sacred weapon, he can enhance another on the following round by using another swift action. The warpriest can use this ability a number of rounds per day equal to his warpriest level, but these rounds need not be consecutive.

These bonuses stack with any existing bonuses the weapon might have, to a maximum of +5. The warpriest can enhance a weapon with any of the following weapon special abilities: brilliant energy, defending, disruption, flaming, frost, keen, and shock. In addition, if the warpriest is chaotic, he can add anarchic and vicious. If he is evil, he can add mighty cleaving and unholy. If he is good, he can add ghost touch and holy. If he is lawful, he can add axiomatic and merciful. If he is neutral (with no other alignment components), he can add spell storing and thundering. Adding any of these special abilities replaces an amount of bonus equal to the special ability’s base cost. Duplicate abilities do not stack. The weapon must have at least a +1 enhancement bonus before any other special abilities can be added.

If multiple weapons are enhanced, each one consumes rounds of use individually. The enhancement bonus and special abilities are determined the first time the ability is used each day, and cannot be changed until the next day. These bonuses do not apply if another creature is wielding the weapon, but they continue to be in effect if the weapon otherwise leaves the warpriest’s possession (such as if the weapon is thrown). This ability can be ended as a free action at the start of the warpriest’s turn (that round does not count against the total duration, unless the ability is resumed during the same round). If the warpriest uses this ability on a double weapon, the effects apply to only one end of the weapon.
"""}]
        fervor= [
{"type": "normal", "text":"""
At 2nd level, a warpriest can draw upon the power of his faith to heal wounds or harm foes. He can also use this ability to quickly cast spells that aid in his struggles. This ability can be used a number of times per day equal to 1/2 his warpriest level + his Wisdom modifier. By expending one use of this ability, a good warpriest (or one who worships a good deity) can touch a creature to heal it of 1d6 points of damage, plus an additional 1d6 points of damage for every 3 warpriest levels he possesses above 2nd (to a maximum of 7d6 at 20th level). Using this ability is a standard action (unless the warpriest targets himself, in which case it’s a swift action). Alternatively, the warpriest can use this ability to harm an undead creature, dealing the same amount of damage he would otherwise heal with a melee touch attack. Using fervor in this way is a standard action that provokes an attack of opportunity. Undead do not receive a saving throw against this damage. This counts as positive energy.

An evil warpriest (or one who worships an evil deity) can use this ability to instead deal damage to living creatures with a melee touch attack and heal undead creatures with a touch. This counts as negative energy.

A neutral warpriest who worships a neutral deity (or one who is not devoted to a particular deity) uses this ability as a good warpriest if he chose to spontaneously cast cure spells or as an evil warpriest if he chose to spontaneously cast inflict spells.

As a swift action, a warpriest can expend one use of this ability to cast any one warpriest spell he has prepared with a casting time of 1 round or shorter. When cast in this way, the spell can target only the warpriest, even if it could normally affect other or multiple targets. Spells cast in this way ignore somatic components and do not provoke attacks of opportunity. The warpriest does not need to have a free hand to cast a spell in this way.
"""}]
        channelEnergy= [
{"type": "normal", "text":"""
Starting at 4th level, a warpriest can release a wave of energy by channeling the power of his faith through his holy symbol. This energy can be used to deal or heal damage, depending on the type of energy channeled and the creatures targeted. Using this ability is a standard action that expends two uses of his fervor ability and doesn’t provoke an attack of opportunity. The warpriest must present a holy symbol to use this ability. A good warpriest (or one who worships a good deity) channels positive energy and can choose to heal living creatures or to deal damage to undead creatures. A neutral warpriest who worships a neutral deity (or one who is not devoted to a particular deity) channels positive energy if he chose to spontaneously cast cure spells or negative energy if he chose to spontaneously cast inflict spells.

Channeling energy causes a burst that affects all creatures of one type (either undead or living) in a 30-foot radius centered on the warpriest. The amount of damage dealt or healed is equal to the amount listed in the fervor ability. Creatures that take damage from channeled energy must succeed at a Will saving throw to halve the damage. The save DC is 10 + 1/2 the warpriest’s level + the warpriest’s Wisdom modifier. Creatures healed by channeled energy cannot exceed their maximum hit point total—all excess healing is lost. A warpriest can choose whether or not to include himself in this effect.
"""}]
        sacredArmor= [
{"type": "normal", "text":"""
At 7th level, the warpriest gains the ability to enhance his armor with divine power as a swift action. This power grants the armor a +1 enhancement bonus. For every 3 levels beyond 7th, this bonus increases by 1 (to a maximum of +5 at 19th level). The warpriest can use this ability a number of minutes per day equal to his warpriest level. This duration must be used in 1-minute increments, but they don’t need to be consecutive.

These bonuses stack with any existing bonuses the armor might have, to a maximum of +5. The warpriest can enhance armor any of the following armor special abilities: energy resistance (normal, improved, and greater), fortification (heavy, light, or moderate), glamered, and spell resistance (13, 15, 17, and 19). Adding any of these special abilities replaces an amount of bonus equal to the special ability’s base cost. For this purpose, glamered counts as a +1 bonus, energy resistance counts as +2, improved energy resistance counts as +4, and greater energy resistance counts as +5. Duplicate abilities do not stack. The armor must have at least a +1 enhancement bonus before any other special abilities can be added.

The enhancement bonus and armor special abilities are determined the first time the ability is used each day and cannot be changed until the next day. These bonuses apply only while the warpriest is wearing the armor, and end immediately if the armor is removed or leaves the warpriest’s possession. This ability can be ended as a free action at the start of the warpriest’s turn. This ability cannot be applied to a shield.

When the warpriest uses this ability, he can also use his sacred weapon ability as a free action by expending one use of his fervor.
"""}]
        aspectOfWar= [
{"type": "normal", "text":"""
At 20th level, the warpriest can channel an aspect of war, growing in power and martial ability. Once per day as a swift action, a warpriest can treat his level as his base attack bonus, gains DR 10/—, and can move at his full speed regardless of the armor he is wearing or his encumbrance. In addition, the blessings he calls upon don’t count against his daily limit during this time. This ability lasts for 1 minute.
"""}]

        ret['Aura'] = aura
        ret['Blessings'] = blessings
        ret['Sacred Weapon'] = sacredWeapon  
        ret['Spellcasting'] = spellcasting

        if self.level >= 2:
            ret['Fervor'] = fervor
        
        if self.level >= 3:
            pass

        if self.level >= 4:
            ret['Channel Energy'] = channelEnergy

        if self.level >= 5:
            pass

        if self.level >= 6:
            pass

        if self.level >= 7:
            ret['Sacred Armor'] = sacredArmor

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
            ret['Aspect of War'] = aspectOfWar

        return ret

    def getSacredWeapon(self):
        ret = {}

        ret['damageDie'] = '1d6'
        ret['totalEnhance'] = 1

        return ret
    
    def getConsumables(self, stats, profBonus):
        ret = {}
        ret['Blessings'] = 3 + math.floor(stats['Wisdom']/2)
        
        if self.level >= 2:
            ret['Fervor'] = 3 + math.floor(self.level/2)
        
        if self.level >= 4:
            ret['Focus Weapon'] = self.level

        return ret

    def getSpells(self, stats, modList):
        ret = {}

        ability    = "Wisdom"
        abilityMod = stats[ability]

        ret['ability']    = ability
        ret['abilityMod'] = abilityMod

        bonus, source = modList.applyModifier("SpellSaveDC")
        source['Base'] = 10
        source[ability] = abilityMod
        source = {k: v for k, v in sorted(source.items(), reverse=True, key=lambda item: item[1])}
        ret['saveDC'] = {'value': 10 + abilityMod + bonus, 'source':source}

        ret['level'] = {}
        ret['level']['Cantrip'] = {}
        ret['level']['1'] = {}
        ret['level']['2'] = {}

        ret['level']['1']['slots'] = 3
        ret['level']['2']['slots'] = 1

        #TODO: Implement this better
        # Get bonus spells from ability score
        ret['level']['1']['slots'] = ret['level']['1']['slots'] + 1
        ret['level']['2']['slots'] = ret['level']['2']['slots'] + 1

        ret['level']['Cantrip']['list'] = {
            "Create Water" : {"source":"Warpriest: Spellcasting" , "timesPrepared":-1, "description":""},
            "Detect Magic" : {"source":"Warpriest: Spellcasting" , "timesPrepared":-1, "description":""},
            "Guidance"     : {"source":"Warpriest: Spellcasting" , "timesPrepared":-1, "description":""},
            "Read Magic"   : {"source":"Warpriest: Spellcasting" , "timesPrepared":-1, "description":""},
        }
        ret['level']['1']['list'] = {
            "Divine Favor"    : {"source":"Warpriest: Spellcasting" , "timesPrepared":2, "description":""},
            "Shield of Faith" : {"source":"Warpriest: Spellcasting" , "timesPrepared":1, "description":""},
            "Unprepared" : {"source":"Warpriest: Spellcasting" , "timesPrepared":1, "description":""},
        }
        ret['level']['2']['list'] = {
            "Cats Grace" : {"source":"Warpriest: Spellcasting" , "timesPrepared":1, "description":""},
            "Ironskin"     : {"source":"Warpriest: Spellcasting" , "timesPrepared":1, "description":""},
        }

        return ret

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
        print(ret['spellAttack']['value'])

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


classes = {}
classes['Warpriest'] = Warpiest(4)
classes['Ranger']    = Ranger(4)
classes['Wizard']    = Wizard(3)