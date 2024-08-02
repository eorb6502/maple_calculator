import json_functions
import spec_skills
import spec_equipment
import spec_combine
def changeStarforce(parts, starforce): #컨버전 스타포스 고려해서 skill 한번 새로고침 해야함
    equipmentDB=json_functions.openjson("./assets/equipment.json")
    dict=equipmentDB[parts]
    starforceDB=json_functions.openjson("./assets/starforce.json")
    stat_flag={
        "str" : 0,
        "dex" : 0,
        "int" : 0,
        "luk" : 0
    }
    hp_arr=[0, 5, 10, 15, 25, 35, 50, 65, 85, 105, 130, 155, 180, 205, 230, 255]
    currentStarforce = dict["스타포스 수치"]
    equipmentTag="일반"
    if dict["이름"].find("타일런트")!=-1:
        equipmentTag="타일런트"
    currentStarforce_stat = dict["스타포스"]
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
    #print(stat_flag)
    starforce_hp=hp_arr[min(starforce, 15)]
    #print(starforce_hp)
    if parts=="무기" or parts=="보조무기":
        weapon_arr=["attack_power", "magic_power"]
        weapon_idx=0
        if dict["기본"]["attack_power"]=="0":
            weapon_idx=1
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
        currentStarforce_stat[weapon_arr[weapon_idx]]=weapon_power-int(dict["강화"][weapon_arr[weapon_idx]])
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
        #print(currentStarforce_stat)
        dict["스타포스 수치"]=starforce
        if parts=="상의" and dict["종류"]=="한벌옷":
            equipmentDB["starforce"]+=2*(starforce-currentStarforce)
        else:
            equipmentDB["starforce"]+=(starforce-currentStarforce)
        json_functions.makejson(equipmentDB, "./assets/equipment.json")
        spec_equipment.make_spec_equipment()
        spec_skills.make_spec_skill(headers = {
        "x-nxopen-api-key": "test_5d1d2bbf3be59f1d5bf961c60a1937b5f5c7d6a8133966a63f38c7ebc5bd3a08efe8d04e6d233bd35cf2fabdeb93fb0d"
        })
        spec_combine.make_spec_final()
def changeJson(parts, stat, sub):
    equipmentDB=json_functions.openjson("./assets/equipment.json")
    dict=equipmentDB[parts][stat]
    for i in sub:
        dict[i]=sub[i]
    json_functions.makejson(equipmentDB, "./assets/equipment.json")
    spec_equipment.make_spec_equipment()
    spec_combine.make_spec_final()

#레벨 제한은 130제면 128~137까지 같은 스텟 공유 -> +2 /10

#이용 예시
#changeStarforce("무기", 18)
#changeJson("무기", "추옵", json)


#아이템 자체를 바꾸게 된다면 세트효과가 변경 될 것이고 그렇다면 어떻게 이를 반영 할 것인가?

