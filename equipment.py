import json
import requests
import json_functions

def make_equipment_data_and_title(data, headers):
    url="https://open.api.nexon.com/maplestory/v1/character/item-equipment"
    #data=json_functions.openjson("./assets/spec.json")
    ocid="?ocid=" + data["ocid"]
    urlString = url + ocid
    response_equip = requests.get(urlString, headers=headers).json()
    """for i in response_equip:
        print(i, response_equip)"""
    equipmentDict={}
    starforce=0
    #print(response_equip["item_equipment"]["무기"])
    for i in response_equip["item_equipment"]:
        #print(i)
        if i["item_equipment_slot"]=="상의" and i["item_equipment_part"]=="한벌옷":
            starforce+=2*int(i["starforce"])
        else:
            starforce+=int(i["starforce"])

        equipmentDict[i["item_equipment_slot"]]={
            "종류" : i["item_equipment_part"],
            "이름" : i["item_name"], 
            "스타포스 수치" : int(i["starforce"]),
            "기본" : i["item_base_option"], \
            "추옵" : i["item_add_option"], \
            "강화" : i["item_etc_option"], \
            "스타포스" : i["item_starforce_option"], \
            "익셉셔널" : i["item_exceptional_option"], \
            "잠재등급" : i["potential_option_grade"], \
            "잠재옵션" : [i["potential_option_1"], i["potential_option_2"], i["potential_option_3"]], \
            "에디등급" : i["additional_potential_option_grade"], \
            "에디옵션" : [i["additional_potential_option_1"], i["additional_potential_option_2"], i["additional_potential_option_3"]], \
            "소울옵션" : i["soul_option"]
            }
    equipmentDict["starforce"]=starforce
    #칭호
    specTitle={
        "str" : 0,
        "dex" : 0,
        "int" : 0,
        "luk" : 0,
        "max_hp" : 0,
        "max_mp" : 0,
        "boss_damage" : 0,
        "normal_damage" : 0,
        "ignore_monster_armor" : 0,
        "critical_rate" : 0,
        "attack_power" : 0,
        "magic_power" : 0,
        "starforce" : 0,
        "exp" : 0,
        "arcane_force": 0,
        "armor" : 0
    }
    if response_equip["title"]!=None:
        titleName=response_equip["title"]["title_name"]
        titleExpire=response_equip["title"]["date_option_expire"]
        #print(titleExpire)
        """
        titleExpireDate=titleExpire.split("T")[0]
        titleExpireTime=titleExpire.split("T")[1].split("+")[0]
        year, month, day = map(int, titleExpireDate.split("-"))
        hour, minute = map(int, titleExpireTime.split(":"))
        timeExpire=year*100000000+month*1000000+day*10000+hour*100+minute
        timeRecent=now.localtime().tm_year*100000000+now.localtime().tm_mon*1000000+now.localtime().tm_mday*10000+now.localtime().tm_hour*100+now.localtime().tm_min
        """
        #print(timeExpire, timeRecent)
        if titleExpire!="expired":
            if titleName=="핑아일체" or titleName=="예아일체":
                specTitle["boss_damage"]+=10
                specTitle["attack_power"]+=5
                specTitle["magic_power"]+=5
                specTitle["str"]+=10
                specTitle["dex"]+=10
                specTitle["int"]+=10
                specTitle["luk"]+=10
            elif titleName=="예티X핑크빈" or titleName=="개화월영":
                specTitle["boss_damage"]+=10
                specTitle["attack_power"]+=10
                specTitle["magic_power"]+=10
                specTitle["str"]+=20
                specTitle["dex"]+=20
                specTitle["int"]+=20
                specTitle["luk"]+=20
                specTitle["max_hp"]+=1000
                specTitle["max_mp"]+=1000
            elif titleName=="메이플을 잘 아는":
                specTitle["ignore_monster_armor"]=1-(1-specTitle["ignore_monster_armor"])*0.9
                specTitle["attack_power"]+=5
                specTitle["magic_power"]+=5
                specTitle["str"]+=10
                specTitle["dex"]+=10
                specTitle["int"]+=10
                specTitle["luk"]+=10
            elif titleName=="킹 오브 루타비스":
                specTitle["boss_damage"]+=5
                specTitle["ignore_monster_armor"]=1-(1-specTitle["ignore_monster_armor"])*0.95
                specTitle["attack_power"]+=3
                specTitle["magic_power"]+=3
                specTitle["str"]+=8
                specTitle["dex"]+=8
                specTitle["int"]+=8
                specTitle["luk"]+=8
                specTitle["max_hp"]+=300
                specTitle["max_mp"]+=300
            elif titleName=="템페스트를 함께한":
                specTitle["ignore_monster_armor"]=1-(1-specTitle["ignore_monster_armor"])*0.95
                specTitle["attack_power"]+=7
                specTitle["magic_power"]+=7
                specTitle["str"]+=7
                specTitle["dex"]+=7
                specTitle["int"]+=7
                specTitle["luk"]+=7
            elif titleName=="내가 제일 잘 나가":
                specTitle["ignore_monster_armor"]=1-(1-specTitle["ignore_monster_armor"])*0.95
                specTitle["attack_power"]+=3
                specTitle["magic_power"]+=3
                specTitle["str"]+=7
                specTitle["dex"]+=7
                specTitle["int"]+=7
                specTitle["luk"]+=7
                specTitle["max_hp"]+=500
                specTitle["max_mp"]+=500
            elif titleName=="챌린지 월드 시즌1 유니크":
                specTitle["boss_damage"]+=10
                specTitle["attack_power"]+=10
                specTitle["magic_power"]+=10
                specTitle["str"]+=10
                specTitle["dex"]+=10
                specTitle["int"]+=10
                specTitle["luk"]+=10
                specTitle["max_hp"]+=500
                specTitle["max_mp"]+=500
            elif titleName=="싸움꾼":
                specTitle["critical_rate"]+=3
            elif titleName=="어벤져":
                specTitle["ignore_monster_armor"]=1-(1-specTitle["ignore_monster_armor"])*0.95
            elif titleName=="베베 클라스!":
                specTitle["ignore_monster_armor"]=1-(1-specTitle["ignore_monster_armor"])*0.95
                specTitle["attack_power"]+=7
                specTitle["magic_power"]+=7
                specTitle["str"]+=7
                specTitle["dex"]+=7
                specTitle["int"]+=7
                specTitle["luk"]+=7
            elif titleName=="영웅이라 불린 자":
                specTitle["attack_power"]+=3
                specTitle["magic_power"]+=3
                specTitle["str"]+=3
                specTitle["dex"]+=3
                specTitle["int"]+=3
                specTitle["luk"]+=3
                specTitle["max_hp"]+=200
                specTitle["max_mp"]+=200
            elif titleName=="히어로 오브 히어로즈":
                specTitle["attack_power"]+=5
                specTitle["magic_power"]+=5
                specTitle["str"]+=5
                specTitle["dex"]+=5
                specTitle["int"]+=5
                specTitle["luk"]+=5
                specTitle["max_hp"]+=200
                specTitle["max_mp"]+=200
            elif titleName=="비행 임무 수행자" or titleName=="위기의 수호자" or titleName=="창공의 에이스" or titleName=="은밀한 스파이" or titleName=="고독의 분쇄자" or titleName=="예리한 명탐정" or titleName=="중력의 반발자" or titleName=="검은 천국의 구원자":
                specTitle["str"]+=1
                specTitle["dex"]+=1
                specTitle["int"]+=1
                specTitle["luk"]+=1
            elif titleName=="견습 헌터 자격증":
                specTitle["str"]+=1
                specTitle["dex"]+=1
                specTitle["int"]+=1
                specTitle["luk"]+=1
                specTitle["max_hp"]+=100
                specTitle["max_mp"]+=100
            elif titleName=="B급 헌터 자격증":
                specTitle["str"]+=2
                specTitle["dex"]+=2
                specTitle["int"]+=2
                specTitle["luk"]+=2
                specTitle["max_hp"]+=200
                specTitle["max_mp"]+=200
            elif titleName=="A급 헌터 자격증":
                specTitle["str"]+=3
                specTitle["dex"]+=3
                specTitle["int"]+=3
                specTitle["luk"]+=3
                specTitle["max_hp"]+=300
                specTitle["max_mp"]+=300
            elif titleName=="S급 헌터 자격증":
                specTitle["attack_power"]+=1
                specTitle["magic_power"]+=1
                specTitle["str"]+=3
                specTitle["dex"]+=3
                specTitle["int"]+=3
                specTitle["luk"]+=3
                specTitle["max_hp"]+=400
                specTitle["max_mp"]+=400
            elif titleName=="나도 사실 잘 나가":
                specTitle["attack_power"]+=2
                specTitle["magic_power"]+=2
                specTitle["str"]+=2
                specTitle["dex"]+=2
                specTitle["int"]+=2
                specTitle["luk"]+=2
                specTitle["max_hp"]+=500
                specTitle["max_mp"]+=500
            elif titleName=="나도 엄청 잘 나가":
                specTitle["attack_power"]+=3
                specTitle["magic_power"]+=3
                specTitle["str"]+=5
                specTitle["dex"]+=5
                specTitle["int"]+=5
                specTitle["luk"]+=5
                specTitle["max_hp"]+=500
                specTitle["max_mp"]+=500
            elif titleName=="플러스 올마이티 데몬":
                specTitle["attack_power"]+=7
                specTitle["magic_power"]+=7
            elif titleName=="플러스 올마이티 제논":
                specTitle["attack_power"]+=7
                specTitle["magic_power"]+=7
            elif titleName=="MVP 브론즈 I": #로마자 한번 테스트
                specTitle["attack_power"]+=1
                specTitle["magic_power"]+=1
            elif titleName=="MVP 브론즈 II":
                specTitle["attack_power"]+=2
                specTitle["magic_power"]+=2
                specTitle["str"]+=4
                specTitle["dex"]+=4
                specTitle["int"]+=4
                specTitle["luk"]+=4
            elif titleName=="MVP 브론즈 II":
                specTitle["attack_power"]+=2
                specTitle["magic_power"]+=2
                specTitle["str"]+=4
                specTitle["dex"]+=4
                specTitle["int"]+=4
                specTitle["luk"]+=4
            elif titleName=="MVP 브론즈 III":
                specTitle["attack_power"]+=3
                specTitle["magic_power"]+=3
                specTitle["str"]+=5
                specTitle["dex"]+=5
                specTitle["int"]+=5
                specTitle["luk"]+=5
            elif titleName=="MVP 브론즈 IV":
                specTitle["attack_power"]+=4
                specTitle["magic_power"]+=4
                specTitle["str"]+=6
                specTitle["dex"]+=6
                specTitle["int"]+=6
                specTitle["luk"]+=6
            elif titleName=="MVP 실버":
                specTitle["attack_power"]+=5
                specTitle["magic_power"]+=5
                specTitle["str"]+=7
                specTitle["dex"]+=7
                specTitle["int"]+=7
                specTitle["luk"]+=7
                specTitle["max_hp"]+=500
                specTitle["max_mp"]+=500
            elif titleName=="MVP 골드":
                specTitle["attack_power"]+=7
                specTitle["magic_power"]+=7
                specTitle["str"]+=8
                specTitle["dex"]+=8
                specTitle["int"]+=8
                specTitle["luk"]+=8
                specTitle["max_hp"]+=500
                specTitle["max_mp"]+=500
            elif titleName=="MVP 다이아":
                specTitle["ignore_monster_armor"]=1-(1-specTitle["ignore_monster_armor"])*0.94
                specTitle["attack_power"]+=10
                specTitle["magic_power"]+=10
                specTitle["str"]+=10
                specTitle["dex"]+=10
                specTitle["int"]+=10
                specTitle["luk"]+=10
                specTitle["max_hp"]+=500
                specTitle["max_mp"]+=500
            elif titleName=="MVP 레드":
                specTitle["ignore_monster_armor"]=1-(1-specTitle["ignore_monster_armor"])*0.92
                specTitle["attack_power"]+=10
                specTitle["magic_power"]+=10
                specTitle["str"]+=10
                specTitle["dex"]+=10
                specTitle["int"]+=10
                specTitle["luk"]+=10
                specTitle["max_hp"]+=1000
                specTitle["max_mp"]+=1000
            elif titleName=="쑥쑥 새싹":
                specTitle["attack_power"]+=5
                specTitle["magic_power"]+=5
                specTitle["str"]+=10
                specTitle["dex"]+=10
                specTitle["int"]+=10
                specTitle["luk"]+=10
                specTitle["max_hp"]+=500
                specTitle["max_mp"]+=500
                specTitle["exp"]+=10
                specTitle["starforce"]+=30
            elif titleName=="입술이 촉촉해":
                specTitle["str"]+=5
                specTitle["dex"]+=5
                specTitle["int"]+=5
                specTitle["luk"]+=5
            elif titleName=="손발이 오글오글":
                specTitle["armor"]+=140
            elif titleName=="내앞에서 연애금지":
                specTitle["attack_power"]+=5
            elif titleName=="먹는게 제일 좋아":
                specTitle["max_hp"]+=300
                specTitle["max_mp"]+=300
            elif titleName=="오징어 아닙니다.":
                specTitle["magic_power"]+=1
            elif titleName=="마스터 엑소시스트":
                specTitle["boss_damage"]+=5
                specTitle["attack_power"]+=7
                specTitle["magic_power"]+=7
                specTitle["str"]+=15
                specTitle["dex"]+=15
                specTitle["int"]+=15
                specTitle["luk"]+=15
                specTitle["max_hp"]+=750
                specTitle["max_mp"]+=750
            elif titleName=="Keep on Burning":
                specTitle["boss_damage"]+=10
                specTitle["ignore_monster_armor"]=1-(1-specTitle["ignore_monster_armor"])*0.9
                specTitle["attack_power"]+=10
                specTitle["magic_power"]+=10
                specTitle["str"]+=10
                specTitle["dex"]+=10
                specTitle["int"]+=10
                specTitle["luk"]+=10
                specTitle["max_hp"]+=400
                specTitle["max_mp"]+=400
            elif titleName=="Eternal Flame":
                specTitle["boss_damage"]+=10
                specTitle["ignore_monster_armor"]=1-(1-specTitle["ignore_monster_armor"])*0.9
                specTitle["attack_power"]+=15
                specTitle["magic_power"]+=15
                specTitle["str"]+=15
                specTitle["dex"]+=15
                specTitle["int"]+=15
                specTitle["luk"]+=15
                specTitle["max_hp"]+=750
                specTitle["max_mp"]+=750
                specTitle["exp"]+=10
                specTitle["arcane_force"]+=50
            elif titleName=="Infinite Flame":
                specTitle["boss_damage"]+=20
                specTitle["ignore_monster_armor"]=1-(1-specTitle["ignore_monster_armor"])*0.8
                specTitle["attack_power"]+=30
                specTitle["magic_power"]+=30
                specTitle["str"]+=30
                specTitle["dex"]+=30
                specTitle["int"]+=30
                specTitle["luk"]+=30
                specTitle["max_hp"]+=1500
                specTitle["max_mp"]+=1500
                specTitle["exp"]+=20
                specTitle["arcane_force"]+=100
            elif titleName=="시련 위에 핀 꽃" or titleName=="구름 뒤로 숨겨진 달":
                specTitle["boss_damage"]+=10
                specTitle["ignore_monster_armor"]=1-(1-specTitle["ignore_monster_armor"])*0.9
                specTitle["attack_power"]+=10
                specTitle["magic_power"]+=10
                specTitle["str"]+=10
                specTitle["dex"]+=10
                specTitle["int"]+=10
                specTitle["luk"]+=10
                specTitle["max_hp"]+=500
                specTitle["max_mp"]+=500
                specTitle["exp"]+=10
                specTitle["arcane_force"]+=30
                specTitle["starforce"]+=30
            elif titleName=="스완 드림" or titleName=="BLACK" or titleName=="PINK":
                specTitle["boss_damage"]+=10
                specTitle["ignore_monster_armor"]=1-(1-specTitle["ignore_monster_armor"])*0.9
                specTitle["attack_power"]+=15
                specTitle["magic_power"]+=15
                specTitle["str"]+=15
                specTitle["dex"]+=15
                specTitle["int"]+=15
                specTitle["luk"]+=15
                specTitle["max_hp"]+=750
                specTitle["max_mp"]+=750
                specTitle["exp"]+=10
                specTitle["arcane_force"]+=50
                specTitle["starforce"]+=30
            elif titleName=="엘 클리어" or titleName=="진 천사":
                specTitle["normal_damage"]+=30
                specTitle["exp"]+=30
                specTitle["attack_power"]+=30
                specTitle["magic_power"]+=30
            elif titleName=="엘 페일" or titleName=="진 악마" or titleName=="영웅":
                specTitle["boss_damage"]+=30
                specTitle["ignore_monster_armor"]=1-(1-specTitle["ignore_monster_armor"])*0.7
                specTitle["attack_power"]+=30
                specTitle["magic_power"]+=30
            elif titleName=="시그너스 기사단":
                specTitle["normal_damage"]+=30
                specTitle["exp"]+=40
                specTitle["attack_power"]+=30
                specTitle["magic_power"]+=30
            else:
                print("{specTitle} is not yet implemented!")
        #print(specTitle)
    equipmentDict["starforce"]+=specTitle["starforce"]
    json_functions.makejson(equipmentDict, "./assets/equipment.json")
    json_functions.makejson(specTitle, "./assets/spec_title.json")
    return equipmentDict, specTitle
"""make_equipment_data_and_title(headers = {
    "x-nxopen-api-key": "API-KEY"
    })"""