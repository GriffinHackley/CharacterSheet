from .races import Race
from ..modifiers import Modifier, ModifierList

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
        ret = super().getFeatures(darkvision=True)

        ret['Blessing of the Raven Queen'] = [
            {"type": "normal", "text":"""
            As a bonus action, you can magically teleport up to 30 feet to an unoccupied space you can see. You can use this trait a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest. 

            Starting at 3rd level, you also gain resistance to all damage when you teleport using this trait. The resistance lasts until the start of your next turn. During that time, you appear ghostly and translucent.
        """}]

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
