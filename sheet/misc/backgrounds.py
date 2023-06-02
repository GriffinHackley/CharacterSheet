class FifthEditionBackground():
    tools     = []
    languages = []

    def __init__(self, config):
        self.name    = config['name']
        self.feature = {'name':config['feature'], 'feature':features[config['feature']]}
        self.skills  = config['skills']

        if 'tools' in config.keys():
            self.tools = config['tools']
        
        if 'languages' in config.keys():
            self.languages = config['languages']


features = {}

features['Wanderer'] = [
{"type": "normal", "text":"""
You have an excellent memory for maps and geography, and you can always recall the general layout of terrain, settlements, and other features around you. In addition, you can find food and fresh water for yourself and up to five other people each day, provided that the land offers berries, small game, water, and so forth.
"""},
]

features['Spirit Medium'] = [
{"type": "normal", "text":"""
After a fateful experience, you believe you’re aligned with spirits and can serve as a conduit for their insights and goals. You have advantage on any Arcana or Religion check you make to remember or research information about spirits and the afterlife. Additionally, you begin your adventuring career with a custom-made device for communing with otherworldly forces, a tarokka deck. Add your proficiency bonus to any ability check you make using this type of divining tool.
"""},
]