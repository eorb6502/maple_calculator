import json
import json_functions
import requests

def make_spec_union(data, headers):
    #print("------------------union start------------------")
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
    spec={
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
        "cooldown_rate": 0
    }
    url="https://open.api.nexon.com/maplestory/v1/user/union"
    #data=json_functions.openjson("./assets/spec.json")
    ocid="?ocid=" + data["ocid"]
    characterLevel=data["level"]
    urlString = url + "-raider" +ocid
    response_raider= requests.get(urlString, headers=headers).json()
    raider_effects=[]
    for i in response_raider["union_raider_stat"]: #+ response_raider["union_occupied_stat"]:
        raider_effects.append(i.lower())
    #print(raider_effects)
    for i in raider_effects:
        mercedes_check=0
        if i.find("확률로")!=-1:
            continue
        if i.find("스킬 재사용 대기시간")!=-1:
            mercedes_check=1
        if mercedes_check==1:
            i=i.split(" 감소")[0]
        else:
            i=i.split(" 증가")[0]
        statAmount=i.split()[-1]
        statName=i.split(" "+statAmount)[0]
        #print(statName, statAmount)
        statNamearr=[]
        tmp=[]
        for i in statName.split(", "):
            tmp.append(i.split("/"))
        #print(tmp)
        for i in tmp:
            for j in i:
                if j not in spec:
                    if j not in specDict:
                        continue
                    statNamearr.append(specDict[j])
                else:
                    statNamearr.append(j)
        #print(statNamearr)
        if len(statNamearr)==0: continue
        for statName in statNamearr:
            if (statName=="max_hp" or statName=="max_mp") and statAmount[-1]=="%":
                statName+="_rate"
            if statAmount[-1]=="%":
                statAmount=statAmount[:-1]
            if statName=="ignore_monster_armor":
                spec[statName]=1-(1-spec[statName])*(1-0.01*float(statAmount))
            else:
                if statName=="str" or statName=="dex" or statName=="int" or statName=="luk" or statName=="max_hp" or statName=="max_mp":
                    statName+="_wo_rate"
                spec[statName]+=float(statAmount)
    #print(spec)
    occupied_effects=[]
    for i in response_raider["union_occupied_stat"]:
        occupied_effects.append(i.lower())
    #print(occupied_effects)
    for i in occupied_effects:
        i=i.split(" 증가")[0]
        statAmount=i.split()[-1]
        statName=i.split(" "+statAmount)[0]
        #print(statName, statAmount)
        if statName not in spec:
            if statName not in specDict:
                continue
            else:
                statName=specDict[statName]
        if statAmount[-1]=="%":
            statAmount=statAmount[:-1]
        if statName=="ignore_monster_armor":
            spec[statName]=1-(1-spec[statName])*(1-0.01*float(statAmount))
        else:
            spec[statName]+=float(statAmount)
    #print(spec)
    #아티팩트
    artifactLevel={
        "올스탯 증가" : 0,
        "최대 HP/MP 증가" :0,
        "공격력/마력 증가" : 0,
        "데미지 증가" : 0,
        "보스 몬스터 공격 시 데미지 증가" : 0,
        "몬스터 방어율 무시 증가" : 0,
        "버프 지속시간 증가" : 0,
        "아이템 드롭률 증가" : 0,
        "메소 획득량 증가" : 0,
        "크리티컬 확률 증가" : 0,
        "크리티컬 데미지 증가" : 0,
        "추가 경험치 획득 증가" : 0
    }
    urlString = url + "-artifact" +ocid
    response_artifact= requests.get(urlString, headers=headers).json()
    #print(response_artifact["union_artifact_effect"])
    for i in response_artifact["union_artifact_crystal"]:
        if i["validity_flag"]=='1':
            continue
        if i["crystal_option_name_1"] in artifactLevel:
            artifactLevel[i["crystal_option_name_1"]]+=i["level"]
        if i["crystal_option_name_2"] in artifactLevel:
            artifactLevel[i["crystal_option_name_2"]]+=i["level"]
        if i["crystal_option_name_3"] in artifactLevel:
            artifactLevel[i["crystal_option_name_3"]]+=i["level"]
    for i in artifactLevel:
        if artifactLevel[i]>=10:
            artifactLevel[i]=10
    #print(artifactLevel)
    for i in artifactLevel:
        level=artifactLevel[i]
        #print(i)
        if i=="올스탯 증가":
            spec["str"]+=15*level
            spec["dex"]+=15*level
            spec["int"]+=15*level
            spec["luk"]+=15*level
        elif i=="최대 HP/MP 증가":
            spec["max_hp"]+=750*level
            spec["max_mp"]+=750*level
        elif i=="공격력/마력 증가":
            spec["attack_power"]+=3*level
            spec["magic_power"]+=3*level
        elif i=="데미지 증가":
            spec["damage"]+=1.5*level
        elif i=="보스 몬스터 공격 시 데미지 증가":
            spec["boss_damage"]+=1.5*level
        elif i=="몬스터 방어율 무시 증가":
            spec["ignore_monster_armor"]=1-(1-spec["ignore_monster_armor"])*(1-0.02*level)
        elif i=="버프 지속시간 증가":
            spec["buff"]+=2*level
        elif i=="아이템 드롭률 증가":
            spec["item_drop"]+=level+int(level/5)
        elif i=="메소 획득량 증가":
            spec["meso_drop"]+=level+int(level/5)
        elif i=="크리티컬 확률 증가":
            spec["critical_rate"]+=2*level
        elif i=="크리티컬 데미지 증가":
            spec["critical_damage"]+=0.4*level
        elif i=="추가 경험치 획득 증가":
            spec["exp"]+=level+int(level/5)
    print(spec)
    json_functions.makejson(spec, "./assets/spec_union.json")
    return spec
