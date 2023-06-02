id = 4

def apply(character):
    character.id = id
    character.config = {"edition":"5e", "critType":'doubleDice',"castingType":"ritual"}
    character.name = "Ezekiel"
    character.baseStats = '10,15,12,12,13,15'
    character.alignment = "Lawful Neutral"
    character.charClass = {"name":"Rogue", "options":{}}
    character.level = 2
    character.background = {'name':"Spirit Medium", 'feature':'Spirit Medium', "skills":["Arcana", "Religion"], "tools":["Playing Cards", "Weaver's Tools"]}
    character.feats = []
    character.race = {"name":"Custom Lineage", "options":{"abilityDistribution":"1/1","primaryAbility":"Dexterity","secondaryAbility":"Charisma", "size":"Small", "feat":{"name":"Ritual Caster", "options":{"class":"Wizard"}}, "languages":["One other language"], "misc":{'variable trait':'darkvision'}}}
    character.playerName = "Griffin"
    character.weapon = [
        {"name" : "Rapier" , "bonus":0 , "damageDie" : "1d8",  "damageType": "P", "toHitAbility": "Dexterity", "damageAbility": 'Dexterity' ,'properties':["Finesse"], 'tags':["Melee"]},
        {"name" : "Dagger" , "bonus":0 , "damageDie" : "1d6",  "damageType": "P", "toHitAbility": "Dexterity", "damageAbility": 'Dexterity' ,'properties':["Finesse", "Light", "Thrown (20/60)"], 'tags':["Melee"]},
    ]
    character.equipment = {
        "head"     : {"name":""},
        "headband" : {"name":""},
        "eyes"     : {"name":""},
        "shoulders": {"name":""},
        "neck"     : {"name":""},
        "chest"    : {"name":""},
        "body"     : {"name":""},
        "armor"    : {"name":"Leather", "armorBonus" : 1, "ability":"Dex", "maxAbility": 20, "armorCheck" : 0, "spellFailure" : 0, "modifiers": []},
        "belt"     : {"name":""},
        "wrists"   : {"name":""},
        "hands"    : {"name":""},
        "ring1"    : {"name":""},
        "ring2"    : {"name":""},
        "feet"     : {"name":""},
    }

    character.accentColor = ["blueviolet", "chartreuse"]

    character.flavor = {
        "backstory":"""
            I was born in the Village of Barovia. When I was young, the spirits started talking to me. They told me of events that had happened, their lives and histories.  The spirits I talk to are Spirits Exekiel talks to. I rarely received visions from the spirits. When I did, it was always a moment from their lives. A moment from the past.
            I remember my first vision of the future distinctly. I remember seeing discontent in the town growing. A rage, directed towards Strahd, cultivating. I remember the townspeople marching towards Strahd's castle, my brother at their head. I remember my brother being ripped in half by Strahd's bare hands and our fellow townspeople being slaughtered, one after the other.
            Madame Eva felt this outburst of psychic energy. As one of the most powerful psychics ever, she knew what the fate of these people were. She watched me from a distance for a time. Watched as I tried to quell my brothers and my fellows discontent with Strahd. I tried my best to forstall the future that I knew was coming. No one believed me when I told them of their fate, not even my brother.
            As the time grew nearer to when this revolt would happen, Madame Eva made her introductions to me. She gave me a taste of the knowledge she had about psychic affairs. Teased me with more information, but always held back what I knew to be the most tantalizing learnings. I learned much from her in that time, and have learned much from her since then. She offered me a place as her apprentice. She promised that, should I go with her, she would no longer hold back in her teachings. Her knowledge would be mine. 
            I did everything I could to stop the Attack on Ravenloft. In the end, I did not affect the outcome. The night that the attack was to take place, I followed Madame Eva out of town that had been my home.
            I was taken in by Madame Eva, a Vistani elder. She trained me for one purpose: to find a party of heroes that could defeat the [vampire](Strahd) that lords over the valley of Barovia. The Madame has instructed me to bring the heroes to Tser Pool to speak with her. I’m not to reveal anything until we’ve spoken to Madame Eva to avoid scaring away our saviors.
        
            Mystery:
            I’d never seen a bottle of Champagne du le Stomp before, and the barkeep didn’t know where the wine was from. As I took a sip of the crimson liquid, a wave of warmth and vitality surged through my body, leaving me feeling somehow more alive than I had in years. The rich, complex flavor of the vintage lingered on my tongue, tantalizing me with its elusive secrets, and I vowed to seek it out again at every tavern I visited. But no matter how many times I asked, it seemed that this strange and wondrous vintage had vanished like a dream, leaving me with only the memory of its fleeting taste.
        """,
        "personalityTraits":"""
            I’m quick to jump to extreme solutions. Why risk a lesser option not working?
        """,
        "flaws":"""
        Internal Fear: That everything is fated / doomed
            External Fear: Wind that extinguishes all light. I’m especially superstitious and live life seeking to avoid bad luck, wicked spirits, or the Mists. 
            Anxious Burper: When I get anxious it is the only time I can ever breathe psychic energy. I am mad about that
            Guilty Pleasure: The finest food and drink
        """,
        "ideals":"""
            Misdirection. I work vigorously to keep others from realizing my flaws or misdeeds.
            Liberation: To free the self or others 
            I decided to turn my natural lucky streak into the basis of a career, though I still realize that improving my skills is essential. 
            I became a criminal because I resented authority in my younger days and saw a life of crime as the best way to fight against tyranny and oppression
        """,
        "bonds":"""
            I’ve seen great darkness, and I’m committed to being a light against it 
            Adversary: The proprietor of an illegal pit fighting arena where you once took bets 
        """
    }

    for item, text in character.flavor.items():
        #Remove first \n
        text = text.replace("\n", "", 1)
        #Reverse text and remove first \n
        rev = text[::-1]
        rev = rev.replace("\n", "", 1)
        #Reverse text again
        text = rev[::-1]

        character.flavor[item] = text

    return character