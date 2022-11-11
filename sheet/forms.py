from django import forms

class ACTypeForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

    choices = [('Normal', 'Normal'), ('Touch','Touch'), ('Flat-Footed', 'Flat-Footed')]
    acType = forms.ChoiceField(choices=choices, label='AC', required=False)

class NailCombatForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""
    
    advantage = forms.BooleanField(label='Advantage', required=False)
    powerAttack = forms.BooleanField(label='Power Attack', required=False)
    twf = forms.BooleanField(label='Two-Weapon Fighting', required=False)
    focusWeapon = forms.BooleanField(label='Focus Weapon', required=False)
    confCrit = forms.BooleanField(label='Confirm Critical', required=False)
    critical = forms.BooleanField(label='Critical', required=False)

class NailSpellForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

    catsGrace = forms.BooleanField(label='Cats Grace', required=False)
    divineFavor = forms.BooleanField(label='Divine Favor', required=False)
    ironSkin = forms.BooleanField(label='Ironskin', required=False)
    shieldOfFaith = forms.BooleanField(label='Shield of Faith', required=False)

class NailSkillForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

    scavenger = forms.BooleanField(label='Scavenger', required=False)

class MyriilCombatForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

    advantage = forms.BooleanField(label='Advantage', required=False)
    powerAttack = forms.BooleanField(label='Sharpshooter', required=False)
    dreadAmbusher = forms.BooleanField(label='Dread Ambusher', required=False)
    favoredFoe = forms.BooleanField(label='Favored Foe', required=False)
    critical = forms.BooleanField(label='Critical', required=False)

class MyriilSpellForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

    absorbElements = forms.BooleanField(label='Absorb Elements', required=False)
    huntersMark = forms.BooleanField(label='Hunters Mark', required=False)