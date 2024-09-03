import requests
import json_functions
def make_spec_set(data, headers):
    specDict={
            "공격력" : "attack_power",
            "마력" : "magic_power",
            "힘" : "str",
            "민첩" : "dex",
            "지력" : "int",
            "운" : "luk",
            "최대 hp" : "max_hp",
            "hp" : "max_hp",
            "보스 몬스터 공격 시 데미지" : "boss_damage",
            "보스 몬스터 공격 시 데미지 증가" : "boss_damage",
            "몬스터 방어율 무시" : "ignore_monster_armor",
            "방어율 무시" : "ignore_monster_armor",
            "일반 몬스터 공격 시 데미지" : "normal_damage",
            "데미지" : "damage",
            "크리티컬 확률" : "critical_rate",
            "크리티컬 데미지" : "critical_damage",
            "최대 mp" : "max_mp",
            "mp": "max_mp",
            "버프 지속시간" : "buff",
            "버프 스킬의 지속시간" : "buff",
            "아케인포스" : "arcane_force",
            "획득 경험치" : "exp",
            "경험치 획득량" : "exp",
            "추가 경험치 획득" : "exp",
            "아이템 드롭률" : "item_drop",
            "메소 획득량" : "meso_drop",
            "올스탯" : "all_stat"
        }
    specSet={
            "str" : 0,
            "str_wo_rate" : 0,
            "str_rate": 0,
            "dex" : 0,
            "dex_wo_rate" : 0,
            "dex_rate": 0,
            "int" : 0,
            "int_wo_rate" : 0,
            "int_rate": 0,
            "luk" : 0,
            "luk_wo_rate" : 0,
            "luk_rate": 0,
            "max_hp" : 0,
            "max_hp_wo_rate" : 0,
            "max_hp_rate": 0,
            "max_mp" : 0,
            "max_mp_wo_rate" : 0,
            "max_mp_rate": 0,
            "attack_power" : 0,
            "attack_power_wo_rate": 0,
            "attack_power_rate" : 0,
            "magic_power" : 0,
            "magic_power_rate" : 0,
            "magic_power_wo_rate": 0,
            "ignore_monster_armor" : 0,
            "boss_damage" : 0,
            "damage" : 0,
            "normal_damage" : 0,
            "critical_rate" : 0,
            "critical_damage" : 0,
            "armor": 0,
            "proficiency": 0,
            "buff": 0,
            "arcane_force": 0,
            "exp": 0,
            "item_drop": 0,
            "meso_drop": 0,
            "insight": 0,
            "cooldown_rate": 0,
            "petSet": []
        }
    #file_path="./assets/spec.json"
    url="https://open.api.nexon.com/maplestory/v1/character/set-effect"
    #data=json_functions.openjson(file_path)
    ocid="?ocid=" + data["ocid"]
    urlString = url + ocid
    response_set = requests.get(urlString, headers=headers).json()
    characterClass=data["class"]
    for i in response_set["set_effect"]:
        print(i)
        set_cnt=i["total_set_count"]
        for j in i["set_effect_info"]:
            #print(j)
            setOption=j["set_option"]
            if setOption.find("스킬 사용 가능")!=-1:
                petSkill=setOption.split(" 스킬 사용 가능")[0][1:-1]
                specSet["petSet"].append(petSkill)
                continue
            setOption=setOption.lower().split(", ")
            print(setOption)
            for k in setOption:
                statName, statAmount = k.split(" : +")
                #print(statName, statAmount)
                if statName not in specSet:
                    if statName not in specDict:
                        continue
                    statName=specDict[statName]
                if (statName=="str" or statName=="dex" or statName=="int" or statName=="luk" or statName=="max_hp" or statName=="max_mp") and statAmount[-1]=="%":
                    statName+="_rate"
                if statAmount[-1]=="%":
                    statAmount=statAmount[:-1]
                if statName=="all_stat":
                    specSet["str"]+=float(statAmount)
                    specSet["dex"]+=float(statAmount)
                    specSet["int"]+=float(statAmount)
                    specSet["luk"]+=float(statAmount)
                elif statName=="ignore_monster_armor":
                    specSet[statName]=1-(1-specSet[statName])*(1-0.01*float(statAmount))
                elif statName=="final_damage":
                    specSet[statName]=(1+specSet[statName])*((1+float(statAmount)))-1
                else:
                    specSet[statName]+=float(statAmount)
    if characterClass=="데몬어벤져":
        specSet["max_hp"]=int(specSet["max_hp"]/2)
    json_functions.makejson(specSet, "./assets/spec_set.json")
    return specSet
"""make_spec_set(headers = {
    "x-nxopen-api-key": "test_5d1d2bbf3be59f1d5bf961c60a1937b5f5c7d6a8133966a63f38c7ebc5bd3a08efe8d04e6d233bd35cf2fabdeb93fb0d"
    })"""