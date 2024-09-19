import json_functions
def calc_spec_w_doping(guild_doping, arr):
    spec_doping={	
        "str": 0,
        "str_rate": 0,
        "dex": 0,
        "dex_rate": 0,
        "int": 0,
        "int_rate": 0,
        "luk": 0,
        "luk_rate": 0,
        "max_hp": 0,
        "max_mp": 0,
        "attack_power": 0,
        "attack_power_wo_weapon": 0,
        "weapon_basic_attack_power": 0,
        "attack_power_rate": 0,
        "magic_power": 0,
        "magic_power_wo_weapon": 0,
        "weapon_basic_magic_power": 0,
        "magic_power_rate": 0,
        "armor": 0,
        "speed": 0,
        "jump": 0,
        "boss_damage": 0,
        "damage": 0,
        "normal_damage": 0,
        "final_damage" : 0,
        "ignore_monster_armor": 0,
        "all_stat": 0,
        "max_hp_rate": 0,
        "max_mp_rate": 0,
        "critical_rate": 0,
        "critical_damage": 0,
        "item_drop": 0,
        "meso_drop": 0,
        "cooldown": 0,
        "starforce": 0
    }
    if arr== None:
        return spec_doping
    #guild_doping=json_functions.openjson("./assets/guild_dopings.json")
    #print(guild_doping)
    for i in arr:
        if i=="보스 킬링 머신":
            spec_doping["boss_damage"]+=2*guild_doping[i]
        elif i=="방어력은 숫자일 뿐":
            spec_doping["ignore_monster_armor"]=1-(1-spec_doping["ignore_monster_armor"]) * (1-0.02*guild_doping[i])
        elif i=="길드의 이름으로":
            spec_doping["damage"]+=2*guild_doping[i]
        elif i=="크게 한방":
            spec_doping["critical_damage"]+=2*guild_doping[i]
        elif i=="향상된 10단계 힘의 물약" or i=="향상된 10단계 힘의 알약":
            spec_doping["str"]+=30
        elif i=="향상된 10단계 민첩의 물약" or i=="향상된 10단계 민첩의 알약":
            spec_doping["dex"]+=30
        elif i=="향상된 10단계 지능의 물약" or i=="향상된 10단계 지능의 알약":
            spec_doping["int"]+=30
        elif i=="향상된 10단계 행운의 물약" or i=="향상된 10단계 행운의 알약":
            spec_doping["luk"]+=30
        elif i=="와헌":
            spec_doping["attack_power_rate"]+=10
            spec_doping["magic_power_rate"]+=10
        elif i=="찐어블":
            spec_doping["attack_power"]+=30
            spec_doping["magic_power"]+=30
            spec_doping["max_hp"]+=750
            spec_doping["max_mp"]+=750
        elif i=="찐샾":
            spec_doping["critical_rate"]+=20
            spec_doping["critical_damage"]+=15
        elif i=="쓸샾":
            spec_doping["critical_rate"]+=10
            spec_doping["critical_damage"]+=8
        elif i=="영메":
            spec_doping["attack_power_rate"]+=4
            spec_doping["magic_power_rate"]+=4
        elif i=="유니온의 힘":
            spec_doping["attack_power"]+=30
            spec_doping["magic_power"]+=30
        elif i=="mvp 슈퍼파워":
            spec_doping["attack_power"]+=30
            spec_doping["magic_power"]+=30
        elif i=="우뿌":
            spec_doping["attack_power"]+=30
            spec_doping["magic_power"]+=30
        elif i=="붕뿌":
            spec_doping["attack_power"]+=30
            spec_doping["magic_power"]+=30
        elif i=="인기도 버프(250)":
            spec_doping["attack_power"]+=40
            spec_doping["magic_power"]+=40
        elif i=="인기도 버프(275)":
            spec_doping["attack_power"]+=50
            spec_doping["magic_power"]+=50
        elif i=="길축":
            spec_doping["attack_power"]+=20
            spec_doping["magic_power"]+=20
        elif i=="길더축":
            spec_doping["attack_power"]+=30
            spec_doping["magic_power"]+=30
        elif i=="반황별":
            spec_doping["attack_power"]+=20
            spec_doping["magic_power"]+=20
        elif i=="반파별":
            spec_doping["ignore_monster_armor"]=1-(1-spec_doping["ignore_monster_armor"]) * 0.8
        elif i=="반빨별":
            spec_doping["boss_damage"]+=20
        elif i=="고급 보스 킬러의 비약":
            spec_doping["boss_damage"]+=20
        elif i=="고급 대영웅의 비약":
            spec_doping["damage"]+=10
        elif i=="고급 관통의 비약":
            spec_doping["ignore_monster_armor"]=1-(1-spec_doping["ignore_monster_armor"]) * 0.8
        elif i=="고급 대축복의 비약":
            spec_doping["str_rate"]+=10
            spec_doping["dex_rate"]+=10
            spec_doping["int_rate"]+=10
            spec_doping["luk_rate"]+=10
        elif i=="전설의 영웅 비약":
            spec_doping["attack_power"]+=30
            spec_doping["magic_power"]+=30
        elif i=="전설의 축복 비약":
            spec_doping["str"]+=10
            spec_doping["dex"]+=10
            spec_doping["int"]+=10
            spec_doping["luk"]+=10
        elif i=="전설의 체력 비약":
            spec_doping["max_hp"]+=7000
        elif i=="전설의 마나 비약":
            spec_doping["max_mp"]+=7000
        elif i=="익스트림 레드":
            spec_doping["attack_power"]+=30
            spec_doping["max_hp"]+=2000
        elif i=="익스트림 블루":
            spec_doping["magic_power"]+=30
            spec_doping["max_mp"]+=2000
        elif i=="VIP 버프":
            spec_doping["str"]+=15
            spec_doping["dex"]+=15
            spec_doping["int"]+=15
            spec_doping["luk"]+=15
            spec_doping["max_hp"]+=1500
            spec_doping["max_mp"]+=1500
            spec_doping["attack_power"]+=15
            spec_doping["magic_power"]+=15
            spec_doping["damage"]+=15
            spec_doping["ignore_monster_armor"]=1-(1-spec_doping["ignore_monster_armor"]) * 0.85
        elif i=="아기 용의 이유식":
            spec_doping["attack_power"]+=7
        elif i=="무기 제련":
            spec_doping["critical_damage"]+=3
        elif i=="고급 무기 제련":
            spec_doping["critical_damage"]+=5
        elif i=="세이람의 영약":
            spec_doping["max_hp"]+=1750
            spec_doping["max_mp"]+=1750
            spec_doping["attack_power_rate"]+=10
            spec_doping["magic_power_rate"]+=10
            spec_doping["boss_damage"]+=10
            spec_doping["critical_damage"]+=16
            spec_doping["critical_rate"]+=20
        else:
            print(i+" is not implemented yet")
    return spec_doping
"""doping_list=["보스 킬링 머신", "방어력은 숫자일 뿐", "길드의 이름으로", "크게 한방", "향상된 10단계 힘의 물약", "향상된 10단계 민첩의 물약", "향상된 10단계 지능의 물약", "향상된 10단계 행운의 물약", "와헌", "찐어블", "찐샾", "영메", "유니온의 힘", "mvp 슈퍼파워", "우뿌", "붕뿌", "인기도 버프(275)", "길더축", "반빨별", "반황별", "인기도 버프(250)", "길축", "반파별", "고급 보스 킬러의 비약", "고급 대영웅의 비약", "고급 관통의 비약", "고급 대축복의 비약", "전설의 영웅 비약", "전설의 축복 비약", "전설의 체력 비약", "전설의 마나 비약", "익스트림 레드", "익스트림 블루", "VIP 버프", "아기 용의 이유식", "무기 제련", "고급 무기 제련"]
calc_spec_w_doping(doping_list)"""