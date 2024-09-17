import json
import json_functions
import requests
import math

def is_float(input_string):
    try:
        float_value = float(input_string)
        return True
    except ValueError:
        return False
def d(x):
    return int(x)
def u(x):
    return int(x+1)
def logcheck(str):
    print(str)
    while str.find("log")!=-1:
        tmp=str[str.find("log"):]
        left=tmp.find("(")
        right=tmp.find(")")
        string=tmp[:right+1]
        deg=tmp[3:left]
        num=tmp[left+1:right]
        print(string, deg, num)
        rep="int(math.Log(" + num + "," + deg+"))"
        str = str.replace(string, rep, 1)
    str=str.lower()
    return str
def make_spec_skill(headers):
    maple_class={
        "str":["히어로", "팔라딘", "다크나이트", "소울마스터", "미하일", "블래스터", "데몬슬레이어", "아란", "카이저", "아델", "제로", "핑크빈", "바이퍼", "캐논마스터", "스트라이커", "은월", "아크", "예티"], \
        "dex":["보우마스터", "신궁", "패스파인더", "윈드브레이커", "와일드헌터", "메르세데스", "카인", "캡틴", "메카닉", "엔젤릭버스터"], \
        "int":["아크메이지(불,독)", "아크메이지(썬,콜)", "비숍", "플레임위자드", "배틀메이지", "에반", "루미너스", "일리움", "라라", "키네시스"], \
        "luk":["나이트로드", "섀도어", "듀얼블레이드", "나이트워커", "팬텀", "카데나", "칼리", "호영"]
    }
    specDict={
        "공격력" : "attack_power",
        "마력" : "magic_power",
        "힘" : "str",
        "민첩" : "dex",
        "지력" : "int",
        "운" : "luk",
        "최대 HP" : "max_hp",
        "HP" : "max_hp",
        "보스 몬스터 공격 시 데미지" : "boss_damage",
        "몬스터 방어율 무시" : "ignore_monster_armor",
        "일반 몬스터 공격 시 데미지" : "normal_damage",
        "크리티컬 확률" : "critical_rate",
        "최대 MP" : "max_mp",
        "MP": "max_mp",
        "버프 지속시간" : "buff",
        "아케인포스" : "arcane_force",
        "획득 경험치" : "exp"
    }
    spec=json_functions.openjson("./assets/spec.json")
    petSet=json_functions.openjson("./assets/spec_set.json")["petSet"]
    skillDB=json_functions.openjson("./skill_db/maple_skills_final.json")
    levelShare=json_functions.openjson("./skill_db/level_share.json")
    characterLevel=spec["level"]
    ocid=spec["ocid"]
    passive=json_functions.openjson("passive_class.json")
    characterClass=spec["class"]
    equipmentData=json_functions.openjson("./assets/spec_equipment.json")
    equipmentRawdata=json_functions.openjson("./assets/equipment.json")
    url="https://open.api.nexon.com/maplestory/v1/character/skill?ocid="+ocid+"&character_skill_grade="+"5"
    #getVskill=requests.get(url, headers=headers).json()
    url="https://open.api.nexon.com/maplestory/v1/character/skill?ocid="+ocid+"&character_skill_grade="+"0"
    #get0Skill=requests.get(url, headers=headers).json()
    #print(getVskill)
    passiveEffect=[]
    specSkill={
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
    #1~4차 패시브
    skipName=["HEXA 스탯", "그란디스 여신의 축복"]
    skillDict={}
    skill_id={}
    for idx in range(6, 0, -1):
        url="https://open.api.nexon.com/maplestory/v1/character/skill?ocid="+ocid+"&character_skill_grade="+str(idx)
        skillDict[idx]={}
        getSkill=requests.get(url, headers=headers).json()
        #print(getSkill)
        skillDB__=skillDB[characterClass][getSkill["character_skill_grade"]]
        #print(skillDB__)
        for i in getSkill["character_skill"]:
            x=i["skill_level"]
            skill_names=[i["skill_name"]]
            if skill_names[0] in levelShare[characterClass]:
                skill_names=levelShare[characterClass][skill_names[0]]
            for skill_name in skill_names:
                print(skill_name)
                if skill_name in skipName:
                    continue
                skillDict[idx][skill_name]={}
                skill_id[skill_name]=idx
                for j in skillDB__[skill_name]:
                    if j=="cover":
                        continue
                    elif j=="skill":
                        continue
                    elif j=="damPlus":
                        continue
                    else:
                        skillDict[idx][skill_name][j]=eval(logcheck(skillDB__[skill_name][j]))
    print(skill_id)
    """basicSpec=passive[characterClass]
    if characterClass=="아크메이지(불,독)" or characterClass=="아크메이지(썬,콜)" or characterClass=="비숍" or characterClass=="플레임위자드" or characterClass=="에반":
        if equipmentRawdata["무기"]["종류"]=="완드":
            specSkill["critical_rate"]+=5
    if characterClass=="히어로" and (equipmentRawdata["무기"]["종류"]=="두손도끼" or equipmentRawdata["무기"]["종류"]=="한손도끼"):
        specSkill["damage"]+=5
    #print(basicSpec)
    for i in basicSpec:
        if i in specSkill:
            if i=="ignore_monster_armor":
                specSkill[i]=1-(1-specSkill[i])*(1-basicSpec[i])
            elif i=="final_damage":
                specSkill[i]=(1+specSkill[i])*(1+basicSpec[i])-1
            else:
                specSkill[i]+=basicSpec[i]
        else:
            specSkill[i]=basicSpec[i]
   #0차
    #print(get0Skill)
    #제논의 서플러스 서플라이 올스텟 퍼를 어떻게 적용할 것인가?
    skill0=get0Skill["character_skill"]
    blessLevel=0
    namearr=["매직 서킷", "엘리멘탈 하모니", "엘리멘탈 엑스퍼트","컨버전 스타포스", "트루 석세서", "패이스", "괴이봉인", "리졸브 타임", "정령의 축복", "여제의 축복", "연합의 의지", "무기 제련", "고급 무기 제련", "파괴의 얄다바오트", "리부트", "하이 덱스터러티", "아스완 무녀의 축복"]
    for i in skill0:
        chk=0
        for j in i:
            if isinstance(i[j], str) and i[j].find("재사용 대기시간")>=0:
                chk=1
                break
        if chk==1:
            continue
        name, level, effect=i["skill_name"], i["skill_level"], i["skill_effect"]
        if name in petSet:
            print(name, effect)
            effect=int(effect.split("증가")[0].split()[-1])
            specSkill["attack_power"]+=effect
            specSkill["magic_power"]+=effect
            continue
        if name not in namearr:
            print("no name in arr" + name)
            continue
        if name=="매직 서킷":
            if characterClass=="일리움":
                specSkill["magic_power"]+=int(min(0.2*equipmentData["weapon_basic_magic_power"], 0.5*equipmentData["attack_power_wo_weapon"]))
            else:
                tmp=int(effect.split("%")[0][-2])*0.1
                #print(tmp)
                specSkill["attack_power"]+=int(min(0.2*equipmentData["weapon_basic_attack_power"], tmp*equipmentData["magic_power_wo_weapon"]))
        elif name=="엘리멘탈 하모니": #시그너스
            if characterClass=="스트라이커" or characterClass=="소울마스터":
                specSkill["str"]+=int(characterLevel/2)
            elif characterClass=="윈드브레이커":
                specSkill["dex"]+=int(characterLevel/2)
            elif characterClass=="플레임위자드":
                specSkill["int"]+=int(characterLevel/2)
            elif characterClass=="나이트워커":
                specSkill["luk"]+=int(characterLevel/2)
            else: 
                print("this shouldn't happen")
        elif name=="엘리멘탈 엑스퍼트":
            specSkill["attack_power_rate"]+=10
            specSkill["magic_power_rate"]+=10
        elif name=="컨버전 스타포스":
            starforce=equipmentData["starforce"]
            print(starforce)
            if characterClass=="제논":
                amount=min(int(starforce/10)*7, 70)
                print(amount)
                specSkill["str"]+=amount
                specSkill["dex"]+=amount
                specSkill["luk"]+=amount
            elif characterClass=="데몬어벤져":
                if starforce<=60:
                    specSkill["max_hp"]+=starforce*80
                elif starforce<=100:
                    specSkill["max_hp"]+=starforce*100
                elif starforce<=140:
                    specSkill["max_hp"]+=starforce*120
                elif starforce<=200:
                    specSkill["max_hp"]+=starforce*140
                elif starforce<=220:
                    specSkill["max_hp"]+=starforce*142
                elif starforce<=250:
                    specSkill["max_hp"]+=starforce*144
                elif starforce<=270:
                    specSkill["max_hp"]+=starforce*146
                elif starforce<=290:
                    specSkill["max_hp"]+=starforce*148
                elif starforce<=310:
                    specSkill["max_hp"]+=starforce*150
                elif starforce<=320:
                    specSkill["max_hp"]+=starforce*152
                elif starforce<=330:
                    specSkill["max_hp"]+=starforce*154
                elif starforce<=340:
                    specSkill["max_hp"]+=starforce*156
                elif starforce<=350:
                    specSkill["max_hp"]+=starforce*158
                elif starforce<=360:
                    specSkill["max_hp"]+=starforce*160
                else: #아직 확인 안됨
                    specSkill["max_hp"]+=starforce*162
            else:
                print("this can't happen!!!!")
        elif name == "트루 석세서":
            specSkill["proficiency"]+=0.1
        elif name=="패이스":
            specSkill["critical_damage"]+=level
            specSkill["attack_power_rate"]+=level
        elif name=="괴이봉인":
            specSkill["final_damage"]=((specSkill["final_damage"]+1)*(1+0.01*level)-1)
            specSkill["attack_power_rate"]+=level
        elif name=="리졸브 타임":
            specSkill["final_damage"]=((specSkill["final_damage"]+1)*(1+0.05*level)-1)
            specSkill["critical_rate"]+=level*4
            specSkill["str"]+=10*level
            specSkill["max_hp_rate"]+=3*level
        elif name == "정령의 축복" or name=="여제의 축복":
            blessLevel=max(blessLevel, level)
        elif name == "연합의 의지":
            specSkill["str"]+=5
            specSkill["dex"]+=5
            specSkill["int"]+=5
            specSkill["luk"]+=5
            specSkill["attack_power"]+=5
            specSkill["magic_power"]+=5
        elif name == "무기 제련":
            specSkill["critical_damage"]+=3
        elif name == "고급 무기 제련":
            specSkill["critical_damage"]+=5
        elif name == "파괴의 얄다바오트":
            specSkill["final_damage"]=(1+specSkill["final_damage"])*1.1-1
        elif name =="리부트":
            reboot_fin_damage=0
            if characterLevel<=99:
                reboot_fin_damage=0.15
            elif characterLevel<=149:
                reboot_fin_damage=0.2
            elif characterLevel<=199:
                reboot_fin_damage=0.25
            elif characterLevel<=249:
                reboot_fin_damage=0.35
            else:
                reboot_fin_damage=0.45
            specSkill["final_damage"]=(1+specSkill["final_damage"])*(1+reboot_fin_damage)-1
            specSkill["attack_power"]+=5
            specSkill["magic_power"]+=5
            specSkill["max_hp"]+=200
            specSkill["max_mp"]+=200
        elif name=="하이 덱스터러티":
            specSkill["dex"]+=40
        else:
            if effect == None or effect.find("증가")==-1 :
                continue
            effectLines=effect.split("\n")
            for i in effectLines:
                print(i)
                te=i.split("증가")[0].strip()
                te=te.replace("/", ", ").split(", ")
                for j in range(0, len(te)):
                    tmp=te[j].split(" ")[-1]
                    if not tmp[-1].isnumeric():
                        tmp=tmp[:-1]
                    #print(tmp)
                    if not is_float(tmp):
                        te[j]+=" "+te[-1].split(" ")[-1]
                rate_check=0
                for j in te:
                    amount=j.split()[-1]
                    value=j.split(" "+amount)[0]
                    if not amount[-1].isnumeric():
                        if amount[-1]=="%":
                            rate_check=1
                        amount=amount[:-1]
                    amount=float(amount)
                    if value not in specDict and value != "올스탯":
                        continue
                    if value != "올스탯":
                        value=specDict[value]
                    if rate_check==1 and (value=="attack_power" or value=="magic_power" or value=="str" or value=="dex" or value=="int" or value=="luk" or value=="max_hp" or value=="max_mp"):
                        value+="_rate"
                    if value=="ignore_monster_armor":
                        specSkill[value]=1-(1-specSkill[value])*(1-0.01*amount)
                    elif value=="올스탯":
                        if rate_check==1:
                            specSkill["str_rate"]+=amount
                            specSkill["dex_rate"]+=amount
                            specSkill["int_rate"]+=amount
                            specSkill["luk_rate"]+=amount
                        else:
                            specSkill["str"]+=amount
                            specSkill["dex"]+=amount
                            specSkill["int"]+=amount
                            specSkill["luk"]+=amount
                    else:
                        specSkill[value]+=amount
                #print(te)
    specSkill["attack_power"]+=blessLevel
    specSkill["magic_power"]+=blessLevel
    #5차
    for i in getVskill["character_skill"]:
        #print(i)
        skillEffect=i['skill_effect']
        tmp=skillEffect.split("패시브 효과 : ")
        #print(skillEffect)
        if len(tmp)<2:
            continue
        passiveEffect.append(tmp[1][:-4])
        
        #print("\n")
    #print(passiveEffect)
    for i in range(0, len(passiveEffect)):
        tmp=passiveEffect[i].split(", ")
        if len(tmp)>=2 and len(tmp[0].split(" "))==1:
            amount=" "+ tmp[1].split(" ")[1]
            tmp[0]+=amount
            passiveEffect[i]=tmp[0]+", "+tmp[1]
    #print(passiveEffect)
    for i in passiveEffect:
        tmp=i.split(", ")
        for j in tmp:
            amount=j.split()[-1]
            stat=j.split(" "+amount)[0]
            #print(stat, amount)
            if stat=="올스탯":
                specSkill["str"]+=int(amount)
                specSkill["dex"]+=int(amount)
                specSkill["int"]+=int(amount)
                specSkill["luk"]+=int(amount)
            if stat=="공격력":
                specSkill["attack_power"]+=int(amount)
            if stat=="마력":
                specSkill["magic_power"]+=int(amount)
            if stat=="힘":
                specSkill["str"]+=int(amount)
            if stat=="지력":
                specSkill["int"]+=int(amount)
            if stat=="최대 HP":
                specSkill["max_hp"]+=int(amount)
    #print(specSkill)
    #6차
    url="https://open.api.nexon.com/maplestory/v1/character/hexamatrix-stat?ocid="+ocid
    get_hexa=requests.get(url, headers=headers).json()
    hexaDict=json_functions.openjson("hexa.json")
    #print(get_hexa)
    characterIndex=0

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
            print(stat, amount)
            if stat=="크리티컬 데미지 증가":
                specSkill["critical_damage"]+=amount
            elif stat=="보스 데미지 증가":
                specSkill["boss_damage"]+=amount
            elif stat=="데미지 증가":
                specSkill["damage"]+=amount
            elif stat=="몬스터 방어율 무시":
                specSkill["ignore_monster_armor"]=1-(1-specSkill["ignore_monster_armor"])*(1-0.01*amount)
            elif stat=="공격력 증가":
                specSkill["attack_power"]+=amount
            elif stat=="마력 증가":
                specSkill["magic_power"]+=amount
            elif stat=="주력 스탯 증가":
                amount=amount[characterIndex]
                if characterIndex==1:
                    specSkill["str"]+=amount
                    specSkill["dex"]+=amount
                    specSkill["int"]+=amount
                    specSkill["luk"]+=amount
                elif characterIndex==2:
                    specSkill["max_hp"]+=amount
                else:
                    for i in maple_class:
                        if characterClass in maple_class[i]:
                            mainStat=i
                            break
                    specSkill[mainStat]+=amount
            else:
                print("this naver shouldn't happen")
    #print(specSkill)
    #stat=
    #amount=hexaDict["main"][hexaStat["main_stat_name"]][hexaStat["main_stat_level"]-1]
    #링크
    url="https://open.api.nexon.com/maplestory/v1/character/link-skill?ocid="+ocid
    get_link=requests.get(url, headers=headers).json()
    for i in get_link:
        print(i)
        print(get_link[i])
    links=get_link["character_link_skill"].copy()
    links.append(get_link["character_owned_link_skill"])
    print(links)
    for i in links:
        skillName, skillLevel=i["skill_name"], i["skill_level"]
        print(skillName, skillLevel)
        if skillName.find("임피리컬 널리지")!=-1:
            specSkill["damage"]+=3*(int((skillLevel+1)/2))
            specSkill["ignore_monster_armor"]=1-(1-specSkill["ignore_monster_armor"])*(1-0.03*(int((skillLevel+1)/2)))
        if skillName.find("어드벤쳐러 큐리어스")!=-1:
            specSkill["critical_rate"]+=3*int((skillLevel+1)/2)+(skillLevel+1)%2
        if skillName.find("시프 커닝")!=-1:
            specSkill["damage"]+=3*skillLevel/2
        if skillName.find("파이렛 블레스")!=-1:
            specSkill["str"]+=10*(skillLevel+1)
            specSkill["dex"]+=10*(skillLevel+1)
            specSkill["int"]+=10*(skillLevel+1)
            specSkill["luk"]+=10*(skillLevel+1)
            specSkill["max_hp"]+=175*(skillLevel+1)
            specSkill["max_mp"]+=175*(skillLevel+1)
        if skillName.find("시그너스 블레스")!=-1:
            specSkill["attack_power"]+=5+2*skillLevel
            specSkill["magic_power"]+=5+2*skillLevel
        if skillName=="하이브리드 로직":
            specSkill["str_rate"]+=5*skillLevel
            specSkill["dex_rate"]+=5*skillLevel
            specSkill["luk_rate"]+=5*skillLevel
            specSkill["int_rate"]+=5*skillLevel
        if skillName=="데몬스 퓨리":
            specSkill["boss_damage"]+=5+5*skillLevel
        if skillName=="와일드 레이지":
            specSkill["damage"]+=5*skillLevel
        if skillName=="퍼미에이트":
            specSkill["ignore_monster_armor"]=1-(1-specSkill["ignore_monster_armor"])*(1-0.01*(5+5*skillLevel))
        if skillName=="엘프의 축복":
            specSkill["exp"]+=5+5*skillLevel
        if skillName=="데들리 인스팅트":
            specSkill["critical_rate"]+=5+5*skillLevel
        if skillName=="아이언 윌":
            specSkill["max_hp_rate"]+=5+5*skillLevel
        if skillName=="전투의 흐름":
            specSkill["damage"]+=4*(1+skillLevel)
        if skillName=="이네이트 기프트":
            specSkill["damage"]+=1+2*skillLevel
        if skillName=="무아":
            specSkill["damage"]+=1+5*skillLevel
        if skillName=="자연의 벗":
            specSkill["damage"]+=1+2*skillLevel
            specSkill["normal_damage"]+=3+4*skillLevel
        if skillName=="자신감":
            specSkill["ignore_monster_armor"]=1-(1-specSkill["ignore_monster_armor"])*(1-0.01*(5*skillLevel))
            specSkill["normal_damage"]+=4+5*skillLevel
        if skillName=="륀느의 축복":
            specSkill["ignore_monster_armor"]=1-(1-specSkill["ignore_monster_armor"])*(1-0.01*(2*skillLevel))
        if skillName=="판단":
            specSkill["critical_damage"]+=2*skillLevel
        print(specSkill["damage"])
    #길드
    if spec["guild"]!=None:
        ogid=spec["oguildid"]
        url="https://open.api.nexon.com/maplestory/v1/guild/basic?oguild_id=" + ogid
        #print(url)
        get_guild=requests.get(url, headers=headers).json()
        #print(get_guild)
        for i in get_guild["guild_skill"]:
            if i["skill_name"]=="길드의 매운 맛Ⅰ":
                specSkill["attack_power"]+=2*i["skill_level"]
                specSkill["magic_power"]+=2*i["skill_level"]
            if i["skill_name"]=="내 안에 별 있다":
                specSkill["starforce"]+=5*i["skill_level"]
            if i["skill_name"]=="졸개들은 물렀거라":
                specSkill["normal_damage"]+=3*i["skill_level"]
            if i["skill_name"]=="길드의 매운 맛Ⅱ":
                specSkill["attack_power"]+=2+2*i["skill_level"]
                specSkill["magic_power"]+=2+2*i["skill_level"]
            if i["skill_name"]=="팔방미인":
                print(4+12*i["skill_level"])
                specSkill["str"]+=4+12*i["skill_level"]
                specSkill["dex"]+=4+12*i["skill_level"]
                specSkill["int"]+=4+12*i["skill_level"]
                specSkill["luk"]+=4+12*i["skill_level"]
                specSkill["max_hp"]+=800+400*i["skill_level"]
            if i["skill_name"]=="아케인포스가 함께하기를":
                specSkill["arcane_force"]+=10+5*i["skill_level"]
            if i["skill_name"]=="길드의 매운 맛Ⅲ":
                specSkill["attack_power"]+=3+2*i["skill_level"]
                specSkill["magic_power"]+=3+2*i["skill_level"]
    json_functions.makejson(specSkill, "./assets/spec_skills_new.json") """
"""make_spec_skill(headers = {
    "x-nxopen-api-key": "API-KEY"
    })"""