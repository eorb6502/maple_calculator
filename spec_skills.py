import json
import json_functions
import requests
maple_class={
    "str":["히어로", "팔라딘", "다크나이트", "소울마스터", "미하일", "블래스터", "데몬슬레이어", "아란", "카이저", "아델", "제로", "핑크빈", "바이퍼", "캐논슈터", "스트라이커", "은월", "아크", "예티"], \
    "dex":["보우마스터", "신궁", "패스파인더", "윈드브레이커", "와일드헌터", "메르세데스", "카인", "캡틴", "메카닉", "엔젤릭버스터"], \
    "int":["아크메이지(불,독)", "아크메이지(썬,콜)", "비숍", "플레임위자드", "배틀메이지", "에반", "루미너스", "일리움", "라라", "키네시스"], \
    "luk":["나이트로드", "섀도어", "듀얼블레이드", "나이트워커", "팬텀", "카데나", "칼리", "호영"]
}
headers = {
"x-nxopen-api-key": "test_4cf454573b36e0ef7bddfcd133597df43e86736d0e4d6b693c2928ee6b54a1dbefe8d04e6d233bd35cf2fabdeb93fb0d"
}
ocid=json_functions.openjson("spec.json")["ocid"]
url="https://open.api.nexon.com/maplestory/v1/character/skill?ocid="+ocid+"&character_skill_grade="+"5"
get_skill=requests.get(url, headers=headers).json()
#print(get_skill)
passiveEffect=[]
spec56={
    "str" : 0,\
    "dex" : 0,\
    "int" : 0,\
    "luk" : 0,\
    "max_hp" : 0,\
    "attack_power" : 0,\
    "magic_power" : 0,\
    "ignore_monster_armor" : 0,\
    "boss_damage" : 0,\
    "damage" : 0,\
    "critical_damage" : 0
}
for i in get_skill["character_skill"]:
    #print(i)
    skillEffect=i['skill_effect']
    tmp=skillEffect.split("패시브 효과 : ")
    print(skillEffect)
    if len(tmp)<2:
        continue
    passiveEffect.append(tmp[1][:-4])
    
    print("\n")
print(passiveEffect)
for i in range(0, len(passiveEffect)):
    tmp=passiveEffect[i].split(", ")
    if len(tmp)>=2 and len(tmp[0].split(" "))==1:
        amount=" "+ tmp[1].split(" ")[1]
        tmp[0]+=amount
        passiveEffect[i]=tmp[0]+", "+tmp[1]
print(passiveEffect)
for i in passiveEffect:
    tmp=i.split(", ")
    for j in tmp:
        amount=j.split()[-1]
        stat=j.split(" "+amount)[0]
        print(stat, amount)
        if stat=="올스탯":
            spec56["str"]+=int(amount)
            spec56["dex"]+=int(amount)
            spec56["int"]+=int(amount)
            spec56["luk"]+=int(amount)
        if stat=="공격력":
            spec56["attack_power"]+=int(amount)
        if stat=="마력":
            spec56["magic_power"]+=int(amount)
        if stat=="힘":
            spec56["str"]+=int(amount)
        if stat=="지력":
            spec56["int"]+=int(amount)
        if stat=="최대 HP":
            spec56["max_hp"]+=int(amount)
print(spec56)
url="https://open.api.nexon.com/maplestory/v1/character/hexamatrix-stat?ocid="+ocid
get_hexa=requests.get(url, headers=headers).json()
hexaDict=json_functions.openjson("hexa.json")
#print(get_hexa)
characterIndex=0
characterClass=get_hexa["character_class"]
if characterClass=="제논":
    characterIndex=1
if characterClass=="데몬어벤져":
    characterIndex=2
if len(get_hexa["character_hexa_stat_core"])>=1:
    hexaStat=get_hexa["character_hexa_stat_core"][0]
    #print(hexaStat)
    hexaTag=["main_stat_name", "sub_stat_name_1", "sub_stat_name_2"]
    for i in hexaTag:
        mainsub=i.split("_")[0]
        amount=hexaDict[mainsub][hexaStat[i]][hexaStat[i.replace("name", "level")]-1]
        stat=hexaStat[i]
        #print(stat, amount)
        if stat=="크리티컬 데미지 증가":
            spec56["critical_damage"]+=amount
        elif stat=="보스 몬스터 공격 시 데미지 증가":
            spec56["boss_damage"]+=amount
        elif stat=="데미지 증가":
            spec56["damage"]+=amount
        elif stat=="몬스터 방어율 무시":
            spec56["ignore_monster_armor"]=1-(1-spec56["ignore_monster_armor"])*(1-amount)
        elif stat=="공격력 증가":
            spec56["attack_power"]+=amount
        elif stat=="마력 증가":
            spec56["magic_power"]+=amount
        elif stat=="주력 스탯 증가":
            amount=amount[characterIndex]
            if characterIndex==1:
                spec56["str"]+=amount
                spec56["dex"]+=amount
                spec56["int"]+=amount
                spec56["luk"]+=amount
            elif characterIndex==2:
                spec56["max_hp"]+=amount
            else:
                for i in maple_class:
                    if characterClass in maple_class[i]:
                        mainStat=i
                        break
                spec56[mainStat]+=amount
        else:
            print("this naver shouldn't happen")
print(spec56)
equipmentData=json_functions.openjson("spec_equipment.json")
json_functions.makejson(spec56, "spec_skills.json")
#stat=
#amount=hexaDict["main"][hexaStat["main_stat_name"]][hexaStat["main_stat_level"]-1]
