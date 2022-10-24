from django.shortcuts import get_object_or_404, render

from .models import Character, PathfinderCharacter, FifthEditionCharacter


def index(request):
    character_list = Character.objects.order_by('name')

    context = {
        'character_list': character_list,
    }

    return render(request, 'sheet/index.html', context)

def detail(request, character_id):
    character = get_object_or_404(Character, pk=character_id)

    # character.config = {"edition":"Pathfinder", "critType":'doubleAll'}
    # character.edition = "Pathfinder"
    # character.name = "Nail"
    # character.baseStats = '14,16,14,12,16,8'
    # character.alignment = "Chaotic Neutral"
    # character.charClass = "Warpriest"
    # character.level = 3
    # character.background = "In Their Footsteps"
    # character.feats = {"Level 1:":"Two-Weapon Fighting", "Level 3":"Butterfly Sting", "Warpriest 3":"Combat Reflexes"}
    # character.race = "Half-Orc"
    # character.playerName = "Griffin"
    # character.traits = ["Fate's Favored", "Anatomist"]
    # character.armor = {"name" : "Chain Shirt", "armorBonus" : 4, "ability":"Dex", "maxAbility": 4, "armorCheck" : 2, "spellFailure" : 20, "modifiers": []}
    # character.weapon = [
    #     {"name" : "Kukri", "bonus":1, "damageDie" : "1d4", "critRange":"18-20", "critDamage":2, "damageType": "S", "toHitAbility": "Dexterity", "damageAbility": 'Strength' ,'tags':['TWF','Main']},
    #     {"name" : "Kukri", "bonus":0, "damageDie" : "1d4", "critRange":"18-20", "critDamage":2, "damageType": "S", "toHitAbility": "Dexterity", "damageAbility": 'Strength','tags':['TWF','Off-Hand'] },
    #     {"name" : "Chakram (30ft.)", "bonus":0, "damageDie" : "1d8", "critRange":"20", "critDamage":2, "damageType": "S", "toHitAbility": "Dexterity", "damageAbility": 'Strength', 'tags':['ranged']}
    # ]
    # character.addWeapon({"name" : "Kukri", "bonus":0, "damageDie" : "1d4", "critRange":"18-20", "critDamage":2, "damageType": "S", "toHitAbility": "Dexterity", "damageAbility": 'Strength' })
    # character.skillRanks({
    #     'Heal'         : 1,
    #     'Handle Animal': 1,
    #     'Perception'   : 3,
    #     'Stealth'      : 3,
    #     'Survival'     : 1,
    # })

    # character.config = {"edition":"5e", "critType":'maxDie'}
    # character.name = "Myriil"
    # character.baseStats = '8,17,14,10,15,8'
    # character.alignment = "Lawful Neutral"
    # character.charClass = "Ranger"
    # character.level = 4
    # character.background = "Spy"
    # character.feats = {"Level 4:":"Elven Accuracy", "Gloomstalker Bow":"Sharpshooter"}
    # character.race = "Shadar-Kai"
    # character.playerName = "Griffin"
    # character.armor = {"name" : "Studded Leather", "armorBonus" : 2, "ability":"Dex", "maxAbility": 20, "armorCheck" : 0, "spellFailure" : 0, "modifiers": []}
    # character.weapon = [
    #     {"name" : "Longbow"    , "bonus":0 , "damageDie" : "1d8",  "damageType": "P", "toHitAbility": "Dexterity", "damageAbility": 'Dexterity' ,'properties':["Ammunition","Range(150/600)","Heavy","Two-Handed"] , 'tags':["Ranged"]},
    #     {"name" : "Shortsword" , "bonus":0 , "damageDie" : "1d6",  "damageType": "S", "toHitAbility": "Dexterity", "damageAbility": 'Dexterity' ,'properties':["Finesse","Light"], 'tags':["Melee", "TWF", "Main"]},
    #     {"name" : "Shortsword" , "bonus":0 , "damageDie" : "1d6",  "damageType": "S", "toHitAbility": "Dexterity", "damageAbility": 'Dexterity' ,'properties':["Finesse","Light"], 'tags':["Melee", "TWF", "Off-Hand"]},
    # ]

    if character.config['edition'] == '5e':
        character = FifthEditionCharacter().fromCharacter(character)
    elif character.config['edition'] == 'Pathfinder':
        character = PathfinderCharacter().fromCharacter(character)

    if request.method == 'GET':
        forms = character.getForms(request)
    
    character.build()
    character.fullChar.save()

    return render(request, 'sheet/detail.html', {'character': character, 'skill_list': character.skillList, 'forms':forms })

def create(request):
    # TODO: Implement this
    # test = Character.create("5e", '8,17,14,10,16,8', "Myriil", "Ranger", 4, "Shadar-Kai", 'Spy', "Griffin", "Neutral Good", [], 0, {}, {}, {})
    # test.save()
    return HttpResponse("Created")

def delete(request, character_id):
    character = get_object_or_404(Character, pk=character_id)
    character.delete()
    return HttpResponse("Deleted")