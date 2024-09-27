import json
import requests
import json_functions
def make_spec_HAP(data, headers, hyperstat_flag, ability_flag):
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
        "일반 몬스터 공격 시 데미지 증가" : "normal_damage",
        "데미지" : "damage",
        "크리티컬 확률" : "critical_rate",
        "크리티컬 데미지" : "critical_damage",
        "최대 mp" : "max_mp",
        "mp": "max_mp",
        "버프 지속시간" : "buff",
        "버프 스킬의 지속 시간" : "buff",
        "아케인포스" : "arcane_force",
        "획득 경험치" : "exp",
        "아이템 드롭률" : "item_drop",
        "메소 획득량" : "meso_drop",
        "모든 능력치" : "all_stat"
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
        "max_hp_rate": 0,
        "max_hp_wo_rate": 0,
        "max_mp" : 0,
        "max_mp_rate": 0,
        "max_mp_wo_rate": 0,
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
        "insight": 0
    }
    url="https://open.api.nexon.com/maplestory/v1/character/"
    data=json_functions.openjson("./assets/spec.json")
    ocid="?ocid=" + data["ocid"]
    characterLevel=data["level"]
    #하이퍼
    urlString = url + "hyper-stat" +ocid
    response_hyper= requests.get(urlString, headers=headers).json()
    if hyperstat_flag==0:
        recentPreset=response_hyper["use_preset_no"]
    else:
        recentPreset=hyperstat_flag
    recentHyper=response_hyper["hyper_stat_preset_"+str(recentPreset)]
    #print(recentHyper)
    for i in recentHyper:
        #print(i)
        if i['stat_level']==0 or "stat_type"=="DF/TF/PP" or "stat_name"=="상태 이상 내성":
            continue
        statType, statIncrease=i["stat_type"].lower().split("/"), i["stat_increase"].split()[-2]
        #print(statType, statIncrease)
        if statIncrease[-1]=="%":
            statIncrease=statIncrease[:-1]
        statIncrease=float(statIncrease)
        for j in statType:
            if j not in spec:
                if j not in specDict:
                    continue
                j=specDict[j]
            if j=="str" or j=="dex" or j=="int" or j=="luk":
                j+="_wo_rate"
            if j!="ignore_monster_armor":
                spec[j]+=statIncrease
            else:
                spec[j]=1-(1-spec[j])*(1-0.01*statIncrease)
    print("-----hyper-----")
    print(spec)

    #어빌리티
    urlString = url + "ability" +ocid
    response_ability= requests.get(urlString, headers=headers).json()
    #print(response_ability)
    if ability_flag==0:
        ability_flag=response_ability["preset_no"]
    ability_preset=response_ability["ability_preset_"+str(ability_flag)]["ability_info"]
    abilities=[]
    for i in ability_preset:
        j=i["ability_value"].split(", ")
        for k in j:
            abilities.append(k.lower())
    for i in abilities:
        level=-1
        if i.find("레벨마다")!=-1:
            level=int(i.split(" 레벨마다 ")[0])
            i=i.split(" 레벨마다 ")[-1]
        if i.find("증가")==-1:
            continue
        i=i.split(" 증가")[0]
        statAmount=i.split()[-1]
        statName=i.split(" "+statAmount)[0]
        if statName not in spec:
            if statName not in specDict:
                continue
            statName=specDict[statName]
        #print(level, statName, statAmount)
        if level!=-1:
            spec[statName+"_wo_rate"]+=int(statAmount)*int(characterLevel/level)
        else:
            if statName=="str" or statName=="dex" or statName=="int" or statName=="luk":
                spec[statName+"_wo_rate"]+=int(statAmount)
            elif statName=="all_stat":
                spec["str_wo_rate"]+=int(statAmount)
                spec["dex_wo_rate"]+=int(statAmount)
                spec["int_wo_rate"]+=int(statAmount)
                spec["luk_wo_rate"]+=int(statAmount)
            elif statName=="max_hp" or statName=="max_mp":
                if statAmount[-1]=="%":
                    spec[statName+"_rate"]+=int(statAmount[:-1])
                else:
                    spec[statName+"_wo_rate"]+=int(statAmount)
            else:
                if statAmount[-1]=="%":
                    statAmount=statAmount[:-1]
                spec[statName]+=int(statAmount)
    print("-----ability-----")
    print(spec)
    #성향
    urlString = url + "propensity" +ocid
    response_propensity= requests.get(urlString, headers=headers).json()
    #print(response_propensity)
    charisma = response_propensity["charisma_level"]
    sensibility = response_propensity["sensibility_level"]
    insight = response_propensity["insight_level"]
    willingness = response_propensity["willingness_level"]
    #print(charisma, sensibility, insight, willingness)
    spec["ignore_monster_armor"]=1-(1-spec["ignore_monster_armor"])*(1-0.01*0.5*int(charisma/5))
    spec["max_mp"]+=100*int(sensibility/5)
    spec["buff"]+=int(sensibility/10)
    spec["insight"]+=0.5*int(insight/10)
    spec["max_hp"]+=100*int(willingness/5)
    spec["armor"]+=5*int(willingness/5)
    print("-----propensity-----")
    print(spec)
    json_functions.makejson(spec, "./assets/spec_hyper_ability_propensity.json")
    return spec