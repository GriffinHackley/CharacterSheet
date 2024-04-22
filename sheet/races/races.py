from .. import races
from ..modifiers import Modifier, ModifierList
from ..static.addParagraphTags import addParagraphTags


def allRaces():
    module = __import__("sheet")
    module = getattr(module, "races")

    ret = {}
    for race in races.__all__:
        current = getattr(module, race)
        ret[race] = current

    return ret


def allRacesDict():
    races = allRaces()

    ret = {}
    for race in races:
        ret[race] = getRace(race)().toDict()

    return ret


def getRace(name):
    try:
        races = allRaces()
        raceModule = races[name]
        return getattr(raceModule, name.replace("-", "").replace(" ", ""))
    except:
        error = "{} does not exist in list of available races"
        raise Exception(error.format(name))


class Race:
    name = ""
    abilityScores = ""
    size = ""
    feat = ""
    speed = 30
    size = "Medium"
    languages = []
    skillBonus = []
    features = []
    classSkills = []
    skills = []
    tools = []
    misc = []

    def appendModifiers(self, modList: ModifierList):
        for score, value in self.abilityScores.items():
            modList.addModifier(Modifier(value, score, self.name))

    def addProficiencies(self, proficiencyList):
        # NOTE: skill proficiency is used in place of class skills for pf characters
        proficiencies = [
            {"skills": self.skills},
            {"languages": self.languages},
            {"tools": self.tools},
        ]

        for proficiency in proficiencies:
            for key, value in proficiency.items():
                if not key in proficiencyList.keys():
                    raise Exception(
                        "Key '"
                        + key
                        + "' was found in proficiencies but does not exist"
                    )

                proficiencyList[key] = proficiencyList[key] + value

    def getConsumables(self, abilityScores, profBonus):
        return []

    def getFeat(self):
        if self.feat == "":
            return {}

        return self.feat

    def getFeatures(
        self, darkvision=False, creatureType="You are Humanoid", extraAttributes=[]
    ):
        ret = []

        size = "You are {}".format(self.size)
        speed = "Your walking speed is {} feet.".format(self.speed)

        ret = ret + [
            {
                "name": "Creature Type",
                "text": addParagraphTags(creatureType),
            },
            {
                "name": "Size",
                "text": addParagraphTags(size),
            },
            {
                "name": "Speed",
                "type": "normal",
                "text": addParagraphTags(speed),
            },
        ]

        if darkvision:
            ret = ret + [
                {
                    "name": "Darkvision",
                    "text": addParagraphTags(
                        "You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You discern colors in that darkness only as shades of gray."
                    ),
                }
            ]

        languages = "You can speak, read, and write Common"
        if len(self.languages) == 1:
            languages = languages + " and {}".format(self.languages[0])
        if len(self.languages) > 1:
            for i in range(len(self.languages) - 1):
                languages = languages + ", {}".format(self.languages[i])
            languages = languages + ", and {}".format(
                self.languages[len(self.languages) - 1]
            )

        ret = ret + [{"name": "Languages", "text": addParagraphTags(languages)}]

        return ret

    def setLevel(self, level):
        self.level = level

    def setOptions(self, options):
        for option, value in options.items():
            if option == "skill":
                i = 0
            if hasattr(self, option):
                setattr(self, option, value)
            else:
                raise Exception(
                    "A race option was found in the config that does not exist. Option:"
                    + option
                )

    def __init__(self):
        return

    def toDict(self):
        ret = {}
        ret["features"] = self.getFeatures()
        return ret
