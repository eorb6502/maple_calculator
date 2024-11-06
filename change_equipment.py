import json_functions
import spec_skills
import spec_equipment
import spec_combine
def conversion_starforce(characterClass, starforce):
    if characterClass=="제논":
        amount=min(int(starforce/10)*7, 70)
    elif characterClass=="데몬어벤져":
        if starforce<=60:
            amount=starforce*80
        elif starforce<=100:
            amount=starforce*100
        elif starforce<=140:
            amount=starforce*120
        elif starforce<=200:
            amount=starforce*140
        elif starforce<=220:
            amount=starforce*142
        elif starforce<=250:
            amount=starforce*144
        elif starforce<=270:
            amount=starforce*146
        elif starforce<=290:
            amount=starforce*148
        elif starforce<=310:
            amount=starforce*150
        elif starforce<=320:
            amount=starforce*152
        elif starforce<=330:
            amount=starforce*154
        elif starforce<=340:
            amount=starforce*156
        elif starforce<=350:
            amount=starforce*158
        elif starforce<=360:
            amount=starforce*160
        else: #아직 확인 안됨
            amount=starforce*162
    else:
        print("this can't happen!!!!")
    return amount
def changeStarforce(specFinal, equipmentDB, parts, starforce):
    characterClass = specFinal["class"]
    dict=equipmentDB[parts]
    starforceDB=json_functions.openjson("./db/starforce.json")
    stat_flag={
        "str" : 0,
        "dex" : 0,
        "int" : 0,
        "luk" : 0
    }
    hp_arr=[0, 5, 10, 15, 25, 35, 50, 65, 85, 105, 130, 155, 180, 205, 230, 255]
    currentStarforce = dict["스타포스 수치"]
    if characterClass=="제논" or characterClass=="데몬어벤져": #컨버전 스타포스 반영
        conversion_starforce_stat_diff = conversion_starforce(characterClass, starforce)- conversion_starforce(characterClass, currentStarforce)
        if characterClass=="제논":
            specFinal["str"]+=conversion_starforce_stat_diff
            specFinal["dex"]+=conversion_starforce_stat_diff
            specFinal["luk"]+=conversion_starforce_stat_diff
        elif characterClass=="데몬어벤져":
            specFinal["max_hp"]+=conversion_starforce_stat_diff
    original_sf_stat = dict["스타포스"].copy()
    currentStarforce_stat = dict["스타포스"]
    equipmentTag="일반"
    if dict["이름"].find("타일런트")!=-1:
        equipmentTag="타일런트"
    equipment_level = str(int((dict["기본"]["base_equipment_level"]+2)/10)*10)
    if equipment_level not in starforceDB[equipmentTag]:
        equipment_level="130"
    #print(equipmentTag, currentStarforce, equipment_level)
    for i in stat_flag: ##스타포스 수치 flag
        if dict["강화"][i]!="0":
            stat_flag[i]=1
    for i in stat_flag:
        if dict["기본"][i]!="0":
            stat_flag[i]=2
    stat_arr=["str", "dex", "int", "luk"]
    for i in stat_arr:
        if stat_flag[i]==0:
            continue
        elif stat_flag[i]==1:
            if equipmentTag=="일반":
                currentStarforce_stat[i]=max(0, starforceDB[equipmentTag][equipment_level]["stat"][starforce]-40)
            else:
                currentStarforce_stat[i]=starforceDB[equipmentTag][equipment_level]["stat"][starforce]
        else:
            currentStarforce_stat[i]=starforceDB[equipmentTag][equipment_level]["stat"][starforce]
    #print(stat_flag)
    if parts!="얼굴장식" and parts!="눈장식" and parts!="귀고리" and parts!="신발" and parts!="장갑" and parts!="기계 심장":
        starforce_hp=hp_arr[min(starforce, 15)]
        currentStarforce_stat["max_hp"]=starforce_hp
        currentStarforce_stat["max_mp"]=starforce_hp
    #print(starforce_hp)
    weapon_arr=["attack_power", "magic_power"]
    weapon_idx=0
    if dict["기본"]["attack_power"]=="0":
        weapon_idx=1
    if parts=="무기" or parts=="보조무기":
        weapon_power = int(dict["기본"][weapon_arr[weapon_idx]])+int(dict["강화"][weapon_arr[weapon_idx]])
        cnt=1
        while cnt<=starforce:
            if cnt<=15:
                weapon_power+=int(weapon_power/50)+1
            else:
                break
            cnt+=1   
        if starforce>=16:
            weapon_power+=starforceDB[equipmentTag][equipment_level]["weapon"][starforce-16]
        currentStarforce_stat[weapon_arr[weapon_idx]]=weapon_power-int(dict["강화"][weapon_arr[weapon_idx]])-int(dict["기본"][weapon_arr[weapon_idx]])
    else:
        if parts!="장갑":
            currentStarforce_stat["attack_power"]=starforceDB[equipmentTag][equipment_level]["armor"][starforce]
            currentStarforce_stat["magic_power"]=starforceDB[equipmentTag][equipment_level]["armor"][starforce]
        else:
            currentStarforce_stat["attack_power"]=starforceDB[equipmentTag][equipment_level]["armor"][starforce]+(starforce>=5)*1+(starforce>=7)*1+(starforce>=9)*1+(starforce>=11)*1+(starforce>=13)*1+(starforce>=14)*1+(starforce>=15)*1
            currentStarforce_stat["magic_power"]=starforceDB[equipmentTag][equipment_level]["armor"][starforce]+(starforce>=5)*1+(starforce>=7)*1+(starforce>=9)*1+(starforce>=11)*1+(starforce>=13)*1+(starforce>=14)*1+(starforce>=15)*1
    print(original_sf_stat, currentStarforce_stat)
    #결과값 반영
    for i in original_sf_stat:
        specFinal[i]+=int(currentStarforce_stat[i])-int(original_sf_stat[i])
    if parts=="상의" and dict["종류"]=="한벌옷":
        specFinal["starforce"]+=2*(starforce-currentStarforce)
    else:
        specFinal["starforce"]+=(starforce-currentStarforce)
    #json_functions.makejson(equipmentDB, "./assets/equipment.json")
    #spec_equipment.make_spec_equipment()
    #spec_skills.make_spec_skill(headers = {
    #"x-nxopen-api-key": "API-KEY"
    #})
    #spec_combine.make_spec_final()
    return specFinal
def changeJson(specFinal, parts, stat, sub):
    equipmentDB=json_functions.openjson("./assets/equipment.json")
    dict=equipmentDB[parts][stat]
    for i in sub:
        specFinal[i]+=sub[i]-int(dict[i])
        #dict[i]=sub[i]
    return specFinal
def changeForce(specFinal, parts, amount, tag):
    maple_class={
        "str":["히어로", "팔라딘", "다크나이트", "소울마스터", "미하일", "블래스터", "데몬슬레이어", "아란", "카이저", "아델", "제로", "핑크빈", "바이퍼", "캐논마스터", "스트라이커", "은월", "아크", "예티"], \
        "dex":["보우마스터", "신궁", "패스파인더", "윈드브레이커", "와일드헌터", "메르세데스", "카인", "캡틴", "메카닉", "엔젤릭버스터"], \
        "int":["아크메이지(불,독)", "아크메이지(썬,콜)", "비숍", "플레임위자드", "배틀메이지", "에반", "루미너스", "일리움", "라라", "키네시스"], \
        "luk":["나이트로드", "섀도어", "듀얼블레이더", "나이트워커", "팬텀", "카데나", "칼리", "호영"]
    }
    characterClass = specFinal["class"]
    if characterClass!="제논" and characterClass!="데몬어벤져":
        for i in maple_class:
            chk=0
            for j in maple_class[i]:
                if j==characterClass:
                    chk=1
                    ju_stat=i
                    break
            if chk==1:
                break
    print(ju_stat)
    if parts=="arcane_force":
        specFinal[parts]+=amount
        if tag==1: #스텟은 변동 o
            if characterClass=="제논":
                specFinal["str_wo_rate"]+=int(4.8*amount)
                specFinal["dex_wo_rate"]+=int(4.8*amount)
                specFinal["luk_wo_rate"]+=int(4.8*amount)
            elif characterClass=="데몬어벤져":
                specFinal["max_hp_wo_rate"]+=210*amount
            else:
                specFinal[ju_stat+"_wo_rate"]+=10*amount
    elif parts=="authentic_force":
        specFinal[parts]+=amount
        if tag==1: #스텟은 변동 o
            if characterClass=="제논":
                specFinal["str_wo_rate"]+=int(9.6*amount)
                specFinal["dex_wo_rate"]+=int(9.6*amount)
                specFinal["luk_wo_rate"]+=int(9.6*amount)
            elif characterClass=="데몬어벤져":
                specFinal["max_hp_wo_rate"]+=420*amount
            else:
                specFinal[ju_stat+"_wo_rate"]+=20*amount
    else:
        print("{parts} should format like arcane or authentic")
    return specFinal
#레벨 제한은 130제면 128~137까지 같은 스텟 공유 -> +2 /10

#이용 예시
#changeStarforce("모자", 23)
#changeJson("무기", "추옵", json)


#아이템 자체를 바꾸게 된다면 세트효과가 변경 될 것이고 그렇다면 어떻게 이를 반영 할 것인가?
#장비아이템 및 세트 효과 DB 제작
spec_dict = json_functions.openjson("./assets/spec_final.json")
equipmentDB = json_functions.openjson("./assets/equipment.json")
print(spec_dict)
print(changeStarforce(spec_dict, equipmentDB, "장갑", 23))
print(changeJson(spec_dict, "장갑", "추옵", {"luk" : 1000000}))

print(changeForce(spec_dict, "arcane_force", 100000, 1))
