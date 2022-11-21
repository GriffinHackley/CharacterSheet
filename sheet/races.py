from .modifiers import Modifier, ModifierList

class Race():
    name             = ''
    primaryAbility   = ''
    secondaryAbility = ''
    size             = ''
    speed            = 0
    languages        = [] 
    skillBonus       = []
    features         = []
    classSkills      = []
    skills           = []
    tools            = []

    def appendModifiers(self, modList:ModifierList):
        modList.addModifier(Modifier(2,"untyped", self.primaryAbility, self.name))
        if not self.secondaryAbility == "None":
            modList.addModifier(Modifier(1,"untyped", self.secondaryAbility, self.name))

    def addProficiencies(self, proficiencyList):
        #NOTE: skill proficiency is used in place of class skills
        proficiencies = [{'skills': self.skills}, {'languages':self.languages}, {'tools': self.tools}]

        for proficiency in proficiencies:
            for key,value in proficiency.items():
                if not key in proficiencyList.keys():
                    raise Exception("Key '" + key + "' found in proficiencies that does not exist")
                
                proficiencyList[key] = proficiencyList[key] + value

    def getConsumables(self, profBonus):
        return {}
    
    def __init__(self, options):
        for option, value in options.items():
            if hasattr(self, option):
                setattr(self, option ,value)
            else:
                raise Exception("A race option was found in the config that does not exist. Option:" + option)

class HalfOrc(Race):
    def __init__(self, options):
        options['name'] = "Half-Orc"
        options['size'] = 'M'
        options['speed'] = 30 
        options['languages'] = ["Common", "Orc"] + options['languages']
        options['skills'] = ['Stealth', 'Perception']
        
        super().__init__(options)

    def appendModifiers(self, modList: ModifierList):
        modList.addModifier(Modifier(1,"luck", 'Fortitude', 'Sacred Tattoo'))
        modList.addModifier(Modifier(1,"luck", 'Reflex', 'Sacred Tattoo'))
        modList.addModifier(Modifier(1,"luck", 'Will', 'Sacred Tattoo'))
        
        for mod in self.skillBonus:
            modList.addModifier(mod)

        return super().appendModifiers(modList)

    def getFeatures(self):
        ret = {}

        ret['Attributes'] = [
            {"type": "heading", "text":"Creature Type:"},
            {"type": "normal", "text":"Half-orcs are Humanoid creatures with both the human and orc subtypes."},

            {"type": "heading", "text":"Size:"},
            {"type": "normal", "text":"Half-orcs are Medium creatures and thus have no bonuses or penalties due to their size."},

            {"type": "heading", "text":"Base Speed:"},
            {"type": "normal", "text":"Half-orcs have a base speed of 30 feet."},
        ]

        ret['Scavenger'] = [
            {"type": "normal", "text":"Some half-orcs eke out a leaving picking over the garbage heaps of society, and must learn to separate rare finds from the inevitable dross. Half-orcs with this racial trait receive a +2 racial bonus on Appraise checks and on Perception checks to find hidden objects (including traps and secret doors), determine whether food is spoiled, or identify a potion by taste. This racial trait replaces the intimidating trait."},
        ]

        ret['Sacred Tattoo'] = [
            {"type": "normal", "text":"Many half-orcs decorate themselves with tattoos, piercings, and ritual scarification, which they consider sacred markings. Half-orcs with this racial trait gain a +1 luck bonus on all saving throws. This racial trait replaces orc ferocity."},
        ]

        ret['Fey Thoughts'] = [
            {"type": "normal", "text":"Stealth and Perception are always class skills you. "},
        ]

        ret['Darkvision'] = [
            {"type": "normal", "text":"Half-orcs can see in the dark up to 60 feet."},
        ]

        ret['Orc Blood'] = [
            {"type": "normal", "text":"Half-orcs count as both humans and orcs for any effect related to race."},
        ]

        ret['Languages'] = [
            {"type": "normal", "text":"Half-orcs begin play speaking Common and Orc. You also know [One other language] due to high intelligence"},
        ]

        return ret

class ShadarKai(Race):
    def __init__(self, options):
        options['name'] = "ShadarKai"
        options['size'] = "M"
        options['speed'] = 30
        options['languages'] = options['languages'] + ["Common"]
        options['skills'] = ["Perception"]
        options['tools'] = ["tool1", "tool2"]
        super().__init__(options)

    def appendModifiers(self, modList: ModifierList):
        return super().appendModifiers(modList)

    def getFeatures(self):
        ret = {}

        ret['Attributes'] = [
            {"type": "heading", "text":"Creature Type:"},
            {"type": "normal", "text":"You are a Humanoid. You are also considered an elf for any prerequisite or effect that requires you to be an elf."},

            {"type": "heading", "text":"Size:"},
            {"type": "normal", "text":"You are Medium"},

            {"type": "heading", "text":"Speed:"},
            {"type": "normal", "text":"Your walking speed is 30 feet."},
        ]

        ret['Blessing of the Raven Queen'] = [
            {"type": "normal", "text":"""
            As a bonus action, you can magically teleport up to 30 feet to an unoccupied space you can see. You can use this trait a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest. 

            Starting at 3rd level, you also gain resistance to all damage when you teleport using this trait. The resistance lasts until the start of your next turn. During that time, you appear ghostly and translucent.
        """}]

        ret['Darkvision'] = [
            {"type": "normal", "text":"You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You discern colors in that darkness only as shades of gray."}
        ]

        ret['Fey Ancestry'] = [
            {"type": "normal", "text":"You have advantage on saving throws you make to avoid or end the charmed condition on yourself."}
        ]

        ret['Keen Senses'] = [
            {"type": "normal", "text":"You have proficiency in the Perception skill."}
        ]

        ret['Necrotic Resistance'] = [
            {"type": "normal", "text":"You have resistance to necrotic damage."}
        ]

        ret['Trance'] = [
            {"type": "normal", "text":"""
            You don’t need to sleep, and magic can’t put you to sleep. You can finish a long rest in 4 hours if you spend those hours in a trancelike meditation, during which you retain consciousness. 

            Whenever you finish this trance, you can gain two proficiencies that you don’t have, each one with a weapon or a tool of your choice selected from the Player’s Handbook. You mystically acquire these proficiencies by drawing them from shared elven memory, and you retain them until you finish your next long rest.
            """}]

        ret['Languages'] = [
            {"type": "normal", "text":"You can speak, read, and write Common and Elven"}
        ]

        return ret

class Harengon(Race):
    def __init__(self, options):
        options['name'] = "Harengon"
        options['speed'] = 30
        options['skills'] = ["Perception"]
        options['languages'] = options['languages'] + ["Common"]
        super().__init__(options)

    def appendModifiers(self, modList: ModifierList):
        modList.addModifier(Modifier('Proficiency Bonus',"untyped", 'Initiative', 'Hare Trigger'))
        
        return super().appendModifiers(modList)

    def getConsumables(self, profBonus):
        ret = {}

        ret['Rabbit Hop'] = profBonus

        return ret

    def getFeatures(self):
        ret = {}

        ret['Attributes'] = [
            {"type": "heading", "text":"Creature Type:"},
            {"type": "normal", "text":"You are a Humanoid."},

            {"type": "heading", "text":"Size:"},
            {"type": "normal", "text":"You are Small"},

            {"type": "heading", "text":"Speed:"},
            {"type": "normal", "text":"Your walking speed is 30 feet."},

            {"type": "heading", "text":"Life Span:"},
            {"type": "normal", "text":"Harengons have a life span of about a century."},
        ]

        ret['Hare Trigger'] = [
            {"type": "normal", "text":"You can add your proficiency bonus to your initiative rolls."}
        ]

        ret['Leporine Senses'] = [
            {"type": "normal", "text":"You have proficiency in the Perception skill."}
        ]

        ret['Lucky Footwork'] = [
            {"type": "normal", "text":"When you fail a Dexterity saving throw, you can use your reaction to roll a d4 and add it to the save, potentially turning the failure into a success. You can't use this reaction if you're prone or your speed is 0."}
        ]

        ret['Rabbit Hop'] = [
            {"type": "normal", "text":"As a bonus action, you can jump a number of feet equal to five times your proficiency bonus, without provoking opportunity attacks. You can use this trait only if your speed is greater than 0. You can use it a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest."}
        ]

        ret['Languages'] = [
            {"type": "normal", "text":"You can speak, read, and write Common and Sylvan"}
        ]

        return ret

races = {}
races['Half-Orc'] = HalfOrc
races['Shadar-Kai'] = ShadarKai
races['Harengon'] = Harengon