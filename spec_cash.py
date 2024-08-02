import requests
import json_functions
def updateDict(dict, arr):
    for j in arr:
        ot=j["option_type"].lower()
        ov=j["option_value"]
        if ot.find("최대")!=-1:
            ot="max_"+ot.split()[-1]
        if ot=="공격력":
            ot="attack_power"
        if ot=="마력":
            ot="magic_power"
        dict[ot]+=int(ov)
    return dict
def make_spec_cash(headers):
    specCash={
        "str" : 0,\
        "str_rate": 0,\
        "dex" : 0,\
        "dex_rate": 0,\
        "int" : 0,\
        "int_rate": 0,\
        "luk" : 0,\
        "luk_rate": 0,\
        "max_hp" : 0,\
        "max_hp_rate": 0,\
        "max_mp" : 0,\
        "max_mp_rate": 0,\
        "attack_power" : 0,\
        "attack_power_rate" : 0,\
        "magic_power" : 0,\
        "magic_power_rate" : 0,\
        "ignore_monster_armor" : 0,\
        "boss_damage" : 0,\
        "damage" : 0,\
        "normal_damage" : 0,\
        "critical_damage" : 0,\
        "critical_rate" : 0,\
        "armor": 0,\
        "proficiency": 0,\
        "buff": 0,\
        "arcane_force": 0,\
        "exp": 0,
        "starforce" : 0
    }
    url="https://open.api.nexon.com/maplestory/v1/character/"
    data=json_functions.openjson("./assets/spec.json")
    ocid="?ocid=" + data["ocid"]
    characterClass=data["class"]
    urlString = url + "cashitem-equipment" +ocid
    response_cash= requests.get(urlString, headers=headers).json()
    urlString = url + "pet-equipment" +ocid
    response_pet= requests.get(urlString, headers=headers).json()
    for i in response_cash["cash_item_equipment_base"]:
        """if i["date_expire"]==None:
            continue"""
        print(i["cash_item_option"])
        specCash=updateDict(specCash, i["cash_item_option"])
    print()
    for i in response_pet:
        print(i, response_pet[i])
    for i in range(1, 4):
        i="pet_"+str(i)
        if response_pet[i+"_name"]==None:
            continue
        petEquipment=i+"_equipment"
        print(petEquipment)
        if response_pet[petEquipment]["item_name"]==None:
            continue
        peos=response_pet[petEquipment]["item_option"]
        if len(peos)==0:
            continue
        print(peos)
        specCash=updateDict(specCash, peos)
    print(specCash)
    if characterClass=="데몬어벤져":
        specCash["max_hp"]=int(specCash["max_hp"]/2)
    json_functions.makejson(specCash, "./assets/spec_cash.json")

"""
make_spec_cash(headers = {
    "x-nxopen-api-key": "test_5d1d2bbf3be59f1d5bf961c60a1937b5f5c7d6a8133966a63f38c7ebc5bd3a08efe8d04e6d233bd35cf2fabdeb93fb0d"
    })"""