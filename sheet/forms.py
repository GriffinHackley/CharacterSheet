from django import forms

class ACTypeForm(forms.Form):
    choices = [('Normal', 'Normal'), ('Touch','Touch'), ('Flat-Footed', 'Flat-Footed')]
    acType = forms.ChoiceField(choices=choices, label='AC', required=False)

class NailCombatForm(forms.Form):
    advantage = forms.BooleanField(label='Advantage', required=False)
    twf = forms.BooleanField(label='Two-Weapon Fighting', required=False)
    powerAttack = forms.BooleanField(label='Power Attack', required=False)
    confCrit = forms.BooleanField(label='Confirm Critical', required=False)
    critical = forms.BooleanField(label='Critical', required=False)

class NailSpellForm(forms.Form):
    divineFavor = forms.BooleanField(label='Divine Favor', required=False)
    shieldOfFaith = forms.BooleanField(label='Shield of Faith', required=False)

class NailSkillForm(forms.Form):
    scavenger = forms.BooleanField(label='Scavenger', required=False)

class MyriilCombatForm(forms.Form):
    advantage = forms.BooleanField(label='Advantage', required=False)
    favoredFoe = forms.BooleanField(label='Favored Foe', required=False)
    dreadAmbusher = forms.BooleanField(label='Dread Ambusher', required=False)
    powerAttack = forms.BooleanField(label='Sharpshooter', required=False)
    critical = forms.BooleanField(label='Critical', required=False)

class MyriilSpellForm(forms.Form):
    huntersMark = forms.BooleanField(label='Hunters Mark', required=False)