import json_functions
import spec_doping
def calc_stat(json, stat_name):
    return int(json[stat_name]*(100+json[stat_name+"_rate"])/100)+json[stat_name+"_wo_rate"]
def find_sub(maple_class, class_name):
    sub_dict={
        "str" : "dex",
        "dex" : "str",
        "int" : "luk",
        "luk" : "dex"
    }
    main_stat=[]
    sub_stat=[]
    for i in maple_class:
        if class_name in maple_class[i]:
            main_stat.append(i)
            sub_stat.append(sub_dict[i])
            break
    if class_name=="섀도어" or class_name=="듀얼블레이드" or class_name=="카데나":
        sub_stat.append("str")
    return main_stat, sub_stat
def calc_stats(json):
    maple_class={
        "str":["히어로", "팔라딘", "다크나이트", "소울마스터", "미하일", "블래스터", "데몬슬레이어", "아란", "카이저", "아델", "제로", "핑크빈", "바이퍼", "캐논마스터", "스트라이커", "은월", "아크", "예티"], \
        "dex":["보우마스터", "신궁", "패스파인더", "윈드브레이커", "와일드헌터", "메르세데스", "카인", "캡틴", "메카닉", "엔젤릭버스터"], \
        "int":["아크메이지(불,독)", "아크메이지(썬,콜)", "비숍", "플레임위자드", "배틀메이지", "에반", "루미너스", "일리움", "라라", "키네시스"], \
        "luk":["나이트로드", "섀도어", "듀얼블레이드", "나이트워커", "팬텀", "카데나", "칼리", "호영"]
    }
    if json["class"]=="제논":
        stat = calc_stat(json, "str")+calc_stat(json, "dex")+calc_stat(json, "luk") 
    elif json["class"]=="데몬어벤져":
        pure_hp=(json["level"]*90+545)
        added_hp=calc_stat(json, "max_hp")-pure_hp
        print(pure_hp, added_hp)
        stat=int(pure_hp/3.5)+0.8*int(added_hp/3.5)+calc_stat(json, "str")
    else:
        main_stat, sub_stat=find_sub(maple_class, json["class"])
        stat=4*calc_stat(json,main_stat[0])
        for i in sub_stat:
            stat+=calc_stat(json,i)
    return stat
def combine_specs(dict1, dict2):
    for i in dict2:
        if i in dict1:
            if i=="ignore_monster_armor":
                dict1[i]=1-(1-dict1[i])*(1-dict2[i])
            elif i=="final_damage":
                dict1[i]=(1+dict1[i])*((1+dict2[i]))-1
            else:
                dict1[i]+=dict2[i]
        else:
            dict1[i]=dict2[i]
def calc_level_diff(characterLevel, monsterLevel):
    print(characterLevel, monsterLevel)
    if monsterLevel-4>=characterLevel:
        return max(1-0.025*(monsterLevel-characterLevel),0)
    elif monsterLevel>=characterLevel:
        return 1.1-0.05*(monsterLevel-characterLevel)
    else:
        return min(1.1-0.02*(monsterLevel-characterLevel),1.2)
    
def calc_force_diff(map_info, character_force):
    arcane_force, authentic_force=character_force
    if map_info["tag"]=="None":
        return 1
    elif map_info["tag"]=="arcane":
        tmp=arcane_force/map_info["force"]
        arcane_arr=[0, 0.01, 0.3, 0.5, 0.7, 1, 1.1, 1.3, 1.5]
        arcane_arr_final_damage=[0.1, 0.3, 0.6, 0.7, 0.8, 1, 1.1, 1.3, 1.5]
        for i in range(8):
            if tmp>=arcane_arr[i] and tmp<arcane_arr[i+1]:
                return arcane_arr_final_damage[i]
        return arcane_arr_final_damage[8]
    elif map_info["tag"]=="authentic":
        if map_info["force"]>=authentic_force:
            return max(1-0.01*( map_info["force"]-authentic_force), 0.05)
        else:
            return min(1-0.005*( map_info["force"]-authentic_force), 1.25)
    else:
        print("this should never happen")
def calc_one_line_dmg(specFinal, guild_doping, mode, doping_arr, skill_damage, skill_attack_count, hyper_damage, core_reinforce, mob_info, map_info, core_ignore_monster_armor, skill_ignore_monster_armor, skill_final_damage, skill_normal_monster_damage):
    specFinal["normal_damage"]+=100*skill_normal_monster_damage
    #specFinal=json_functions.openjson("./assets/spec_final.json")
    specDoping=spec_doping.calc_spec_w_doping(guild_doping, doping_arr)
    print(specFinal)
    combine_specs(specFinal, specDoping)
    #print(specFinal)
    stat=calc_stats(specFinal)*0.01
    #print(stat)
    attk=calc_stat(specFinal, "attack_power")

    damage=1+specFinal["damage"]/100+hyper_damage #하이퍼 스킬 보정


    final_damage=(1+0.01*specFinal["final_damage"])*(1+skill_final_damage)*(1+core_reinforce)*calc_level_diff(specFinal["level"], mob_info["level"])*calc_force_diff(map_info, (specFinal["arcane_force"], specFinal["authentic_force"])) #코강, 레벨, 심볼 보정 추가
    print(calc_level_diff(specFinal["level"], mob_info["level"]), calc_force_diff(map_info, (specFinal["arcane_force"], specFinal["authentic_force"])))
    weapon_multiplier=specFinal["weapon_multiplier"]

    ignore_monster_armor=1-(1-0.01*specFinal["ignore_monster_armor"])*(1-core_ignore_monster_armor)*(1-skill_ignore_monster_armor) #스킬 자체 보정, 코강 보정 추가

    monster_armor_multiplier=1-mob_info["armor"]*(1-ignore_monster_armor) # 몬스터 방어율 보정

    proficiency=(1+specFinal["proficiency"])/2

    property = 1-mob_info["property"]*(1-specFinal["insight"]) ##몹 반감 보정

    class_multiplier=1 ###제논, 법사 보정 해야됨
    """if specFinal["class"]=="제논":
        class_multiplier=0.875
    elif specFinal["class"]=="아크메이지(불,독)" or specFinal["class"]=="아크메이지(썬,콜)" or specFinal["class"]=="비숍" or specFinal["class"]=="플레임위자드":
        class_multiplier=1.2"""
    
    critical = 1+min(specFinal["critical_rate"]/100, 1)*(0.35+specFinal["critical_damage"]/100) #계산용 크확 100퍼

    print(specFinal["normal_damage"], stat, attk, damage, final_damage, weapon_multiplier, ignore_monster_armor, monster_armor_multiplier, proficiency, property, critical)
    skill_percentage=skill_damage * skill_attack_count

    stat_attack_power=stat*attk*weapon_multiplier*damage*final_damage

    #normal_damage = class_multiplier*stat*attk*weapon_multiplier*(damage+specFinal["normal_damage"]/100)* final_damage*proficiency*monster_armor_multiplier*critical*property
    #boss_damage =  class_multiplier*stat*attk*weapon_multiplier*(damage+specFinal["boss_damage"]/100)* final_damage*proficiency*monster_armor_multiplier*critical*property
    mode_damage=class_multiplier*stat*attk*weapon_multiplier*(damage+specFinal[mode+"_damage"]/100)* final_damage*proficiency*monster_armor_multiplier*critical*property
    print(mode_damage)
    #print(stat_attack_power, normal_damage * skill_damage, normal_damage * skill_percentage, boss_damage * skill_percentage)
    return int(mode_damage * skill_damage), int(mode_damage*skill_damage*skill_attack_count), specFinal
#print(calc_one_line_dmg("normal",[], 2.9, 8, 0.2, 1.2, {"level" : 260,"armor" : 0.1, "property" : 0}, {"tag" : "authentic", "force" : 30}, 0.2,0))