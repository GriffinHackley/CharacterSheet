from .races import Race
from ..modifiers import Modifier, ModifierList

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
        extraAttributes = [
            {"type": "heading", "text":"Life Span:"},
            {"type": "normal", "text":"Harengons have a life span of about a century."},
        ]

        ret = super().getFeatures(extraAttributes=extraAttributes)


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
