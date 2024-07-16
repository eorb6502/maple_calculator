import json
import json_functions
def calcIgnoreMonstorArmor(arr):
    tmp=1
    for i in arr:
        tmp*=(1-0.01*i)
    return 1-tmp
def setCheck(str):
    bossSet=["아쿠아틱 레터 눈장식", "블랙빈 마크", "파풀라투스 마크", "응축된 힘의 결정석", "골든 클로버 벨트", "분노한 자쿰의 벨트", "혼테일의 목걸이", "카오스 혼테일의 목걸이", "매커네이터 펜던트", "도미네이터 펜던트", "데아시두스 이어링", "지옥의 불꽃", "실버블라썸 링", "고귀한 이피아의 반지", "가디언 엔젤 링", "크리스탈 웬투스 뱃지", "로얄 블랙메탈 숄더", "영생의 돌", "핑크빛 성배"]
    dawnSet=["트와일라이트 마크", "에스텔라 이어링", "데이브레이크 펜던트", "여명의 가디언 엔젤 링"]
    pitchedSet=["루즈 컨트롤 머신 마크", "마력이 깃든 안대", "블랙 하트", "컴플리트 언더컨트롤", "몽환의 벨트", "고통의 근원", "창세의 뱃지", "커맨더 포스 이어링", "거대한 공포", "저주받은 적의 마도서", "저주받은 황의 마도서", "저주받은 청의 마도서", "저주받은 녹의 마도서","미트라의 분노 : 전사", "미트라의 분노 : 궁수", "미트라의 분노 : 마법사", "미트라의 분노 : 도적", "미트라의 분노 : 해적"]
    sheenSet=["근원의 속삭임"]
    rootabisSet=["이글아이", "트릭스터", "하이네스", "파프니르"]
    if str in bossSet:
        return "보스"
    if str in dawnSet:
        return "여명"
    if str in pitchedSet:
        return "칠흑"
    if str in sheenSet:
        return "광휘"
    name=str.split()[0]
    if name in rootabisSet:
        classname=str.split()[1][:3]
        if classname=="워리어":
            return "루타비스 전사"
        elif classname=="던위치":
            return "루타비스 마법사"
        elif classname=="레인져":
            return "루타비스 궁수"
        elif classname=="어새신":
            return "루타비스 도적"
        else:
            return "루타비스 해적"
    return name
def updateSpec(on, oa, ts, ima):
    optionDict={"몬스터 방어율 무시" : "ignore_monster_armor",
                "공격력": "attack_power", 
                "마력": "magic_power", 
                "보스 몬스터 공격 시 데미지": "boss_damage", 
                "데미지": "damage",
                "크리티컬 확률": "critical_rate",
                "크리티컬 데미지": "critical_damage",
                "최대 hp": "max_hp",
                "최대 mp": "max_mp",
                "올스탯": "all_stat",
                "아이템 드롭률": "item_drop", 
                "메소 획득량": "meso_drop",
                "모든 스킬의 재사용 대기시간": "cooldown"
                }
    oa=oa[1:]
    if on in ts:
        print(oa)
        if(oa[-1]=="%"):
            on+="_rate"
            oa=oa[:-1]
        ts[on]+=int(oa)
    else:
        if on in optionDict:
            on=optionDict[on]
            if on=="ignore_monster_armor":
                ima.append(int(oa[:-1]))
            elif on=="boss_damage" or on=="damage" or on=="critical_rate" or on=="critical_damage" or on=="item_drop" or on=="meso_drop":
                ts[on]+=int(oa[:-1])
            elif on=="all_stat":
                if(oa[-1]=="%"):
                    ts[on]+=int(oa[:-1])
                else:
                    ts["str"]+=int(oa)
                    ts["dex"]+=int(oa)
                    ts["int"]+=int(oa)
                    ts["luk"]+=int(oa)
            elif on=="cooldown":
                ts[on]+=int(oa[0])
            else:
                if(oa[-1]=="%"):
                    on+="_rate"
                    oa=oa[:-1]
                ts[on]+=int(oa)

    return ts, ima
def updateSetEffect(es, ts, ima):
    for i in es:
        if i.split()[0]=="루타비스":
            class_name=i.split()[1]
            if es[i]>=2:
                ts["max_hp"]+=1000
                ts["max_mp"]+=1000
                if class_name=="전사" or class_name=="궁수" or class_name=="해적":
                    ts["str"]+=20
                    ts["dex"]+=20
                elif class_name=="마법사":
                    ts["int"]+=20
                    ts["luk"]+=20
                else:
                    ts["luk"]+=20
                    ts["dex"]+=20
            if es[i]>=3:
                ts["max_hp_rate"]+=10
                ts["max_mp_rate"]+=10
                if class_name=="마법사":
                    ts["magic_power"]+=50
                else:
                    ts["attack_power"]+=50
            if es[i]>=4:
                ts["boss_damage"]+=30
        if i=="앱솔랩스":
            if es[i]>=2:
                ts["max_hp"]+=1500
                ts["max_mp"]+=1500
                ts["attack_power"]+=20
                ts["magic_power"]+=20
                ts["boss_damage"]+=10
            if es[i]>=3:
                ts["str"]+=30
                ts["dex"]+=30
                ts["luk"]+=30
                ts["int"]+=30
                ts["attack_power"]+=20
                ts["magic_power"]+=20
                ts["boss_damage"]+=10
            if es[i]>=4:
                ts["attack_power"]+=25
                ts["magic_power"]+=25
                ts["armor"]+=200
                ima.append(10)
            if es[i]>=5:
                ts["attack_power"]+=30
                ts["magic_power"]+=30
                ts["boss_damage"]+=10
            if es[i]>=6:
                ts["max_hp_rate"]+=20
                ts["max_mp_rate"]+=20
                ts["attack_power"]+=20
                ts["magic_power"]+=20
            if es[i]>=7:
                ts["attack_power"]+=20
                ts["magic_power"]+=20
                ima.append(10)
        if i=="아케인셰이드":
            if es[i]>=2:
                ts["attack_power"]+=30
                ts["magic_power"]+=30
                ts["boss_damage"]+=10
            if es[i]>=3:
                ts["attack_power"]+=30
                ts["magic_power"]+=30
                ts["armor"]+=400
                ima.append(10)
            if es[i]>=4:
                ts["str"]+=50
                ts["dex"]+=50
                ts["luk"]+=50
                ts["int"]+=50
                ts["attack_power"]+=35
                ts["magic_power"]+=35
                ts["boss_damage"]+=10
            if es[i]>=5:
                ts["max_hp"]+=2000
                ts["max_mp"]+=2000
                ts["attack_power"]+=40
                ts["magic_power"]+=40
                ts["boss_damage"]+=10
            if es[i]>=6:
                ts["max_hp_rate"]+=30
                ts["max_mp_rate"]+=30
                ts["attack_power"]+=30
                ts["magic_power"]+=30
            if es[i]>=7:
                ts["attack_power"]+=30
                ts["magic_power"]+=30
                ima.append(10)
        if i=="에테르넬":
            if es[i]>=2:
                ts["max_hp"]+=2500
                ts["max_mp"]+=2500
                ts["attack_power"]+=40
                ts["magic_power"]+=40
                ts["boss_damage"]+=10
            if es[i]>=3:
                ts["str"]+=50
                ts["dex"]+=50
                ts["luk"]+=50
                ts["int"]+=50
                ts["attack_power"]+=40
                ts["magic_power"]+=40
                ts["boss_damage"]+=10
                ts["armor"]+=600
            if es[i]>=4:
                ts["max_hp_rate"]+=15
                ts["max_mp_rate"]+=15
                ts["attack_power"]+=40
                ts["magic_power"]+=40
                ts["boss_damage"]+=10
            if es[i]>=5:
                ts["attack_power"]+=40
                ts["magic_power"]+=40
                ima.append(20)
            if es[i]>=6:
                ts["attack_power"]+=40
                ts["magic_power"]+=40
                ts["boss_damage"]+=15
            if es[i]>=7:
                ts["max_hp"]+=2500
                ts["max_mp"]+=2500
                ts["str"]+=50
                ts["dex"]+=50
                ts["luk"]+=50
                ts["int"]+=50
                ts["attack_power"]+=40
                ts["magic_power"]+=40
                ts["boss_damage"]+=15
            if es[i]>=8:
                ts["attack_power"]+=40
                ts["magic_power"]+=40
                ts["boss_damage"]+=15
        if i=="보스":
            if es[i]>=3:
                ts["str"]+=10
                ts["dex"]+=10
                ts["luk"]+=10
                ts["int"]+=10
                ts["max_hp_rate"]+=5
                ts["max_mp_rate"]+=5
                ts["attack_power"]+=5
                ts["magic_power"]+=5
            if es[i]>=5:
                ts["str"]+=10
                ts["dex"]+=10
                ts["luk"]+=10
                ts["int"]+=10
                ts["max_hp_rate"]+=5
                ts["max_mp_rate"]+=5
                ts["attack_power"]+=5
                ts["magic_power"]+=5
            if es[i]>=7:
                ts["str"]+=10
                ts["dex"]+=10
                ts["luk"]+=10
                ts["int"]+=10
                ts["attack_power"]+=10
                ts["magic_power"]+=10
                ts["armor"]+=80
                ima.append(10)
            if es[i]>=9:
                ts["str"]+=15
                ts["dex"]+=15
                ts["luk"]+=15
                ts["int"]+=15
                ts["attack_power"]+=10
                ts["magic_power"]+=10
                ts["armor"]+=100
                ts["boss_damage"]+=10
        if i=="여명":
            if es[i]>=2:
                ts["str"]+=10
                ts["dex"]+=10
                ts["luk"]+=10
                ts["int"]+=10
                ts["max_hp"]+=250
                ts["attack_power"]+=10
                ts["magic_power"]+=10
                ts["boss_damage"]+=10
            if es[i]>=3:
                ts["str"]+=10
                ts["dex"]+=10
                ts["luk"]+=10
                ts["int"]+=10
                ts["max_hp"]+=250
                ts["attack_power"]+=10
                ts["magic_power"]+=10
            if es[i]>=4:
                ts["str"]+=10
                ts["dex"]+=10
                ts["luk"]+=10
                ts["int"]+=10
                ts["max_hp"]+=250
                ts["attack_power"]+=10
                ts["magic_power"]+=10
                ts["armor"]+=100
                ima.append(10)
        if i=="칠흑":
            if es[i]>=2:
                ts["str"]+=10
                ts["dex"]+=10
                ts["luk"]+=10
                ts["int"]+=10
                ts["max_hp"]+=250
                ts["attack_power"]+=10
                ts["magic_power"]+=10
                ts["boss_damage"]+=10
            if es[i]>=3:
                ts["str"]+=10
                ts["dex"]+=10
                ts["luk"]+=10
                ts["int"]+=10
                ts["max_hp"]+=250
                ts["attack_power"]+=10
                ts["magic_power"]+=10
                ts["armor"]+=250
                ima.append(10)
            if es[i]>=4:
                ts["str"]+=15
                ts["dex"]+=15
                ts["luk"]+=15
                ts["int"]+=15
                ts["max_hp"]+=375
                ts["attack_power"]+=15
                ts["magic_power"]+=15
                ts["critical_damage"]+=5
            if es[i]>=5:
                ts["str"]+=15
                ts["dex"]+=15
                ts["luk"]+=15
                ts["int"]+=15
                ts["max_hp"]+=375
                ts["attack_power"]+=15
                ts["magic_power"]+=15
                ts["boss_damage"]+=10
            if es[i]>=6:
                ts["str"]+=15
                ts["dex"]+=15
                ts["luk"]+=15
                ts["int"]+=15
                ts["max_hp"]+=375
                ts["attack_power"]+=15
                ts["magic_power"]+=15
                ts["boss_damage"]+=10
            if es[i]>=7:
                ts["str"]+=15
                ts["dex"]+=15
                ts["luk"]+=15
                ts["int"]+=15
                ts["max_hp"]+=375
                ts["attack_power"]+=15
                ts["magic_power"]+=15
                ts["critical_damage"]+=5
            if es[i]>=8:
                ts["str"]+=15
                ts["dex"]+=15
                ts["luk"]+=15
                ts["int"]+=15
                ts["max_hp"]+=375
                ts["attack_power"]+=15
                ts["magic_power"]+=15
                ts["boss_damage"]+=10
            if es[i]>=9:
                ts["str"]+=15
                ts["dex"]+=15
                ts["luk"]+=15
                ts["int"]+=15
                ts["max_hp"]+=375
                ts["attack_power"]+=15
                ts["magic_power"]+=15
                ts["critical_damage"]+=5
            if es[i]>=10:
                ts["str"]+=20
                ts["dex"]+=20
                ts["luk"]+=20
                ts["int"]+=20
                ts["max_hp"]+=500
                ts["attack_power"]+=20
                ts["magic_power"]+=20
                ts["boss_damage"]+=10
        if i=="광휘":
            continue
        if i=="마이스터":
            if es[i]>=2:
                ts["max_hp_rate"]+=10
                ts["max_mp_rate"]+=10
            if es[i]>=3:
                ts["attack_power"]+=40
                ts["magic_power"]+=40
            if es[i]>=4:
                ts["boss_damage"]+=20
        if i=="칠요의":
            if es[i]>=2:
                ima.append(10)
equipmentSet={"루타비스 전사" : 0, "루타비스 궁수" : 0, "루타비스 마법사" : 0, "루타비스 도적" : 0, "루타비스 해적" : 0, "앱솔랩스" : 0, "아케인셰이드" : 0, "에테르넬" : 0, "보스" : 0, "여명" : 0, "칠흑" : 0, "광휘" : 0, "마이스터" : 0, "칠요의" : 0}
totalStat={	"str": 0,
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
            "attack_power_rate": 0,
			"magic_power": 0,
            "magic_power_rate": 0,
			"armor": 0,
			"speed": 0,
			"jump": 0,
			"boss_damage": 0,
            "damage": 0,
			"ignore_monster_armor": 0,
			"all_stat": 0,
			"max_hp_rate": 0,
			"max_mp_rate": 0,
            "critical_rate": 0,
            "critical_damage": 0,
            "item_drop": 0,
            "meso_drop": 0,
            "cooldown": 0
		}
ignore_monster_armor=[]
equipmentData=json_functions.openjson("equipment.json")
specData=json_functions.openjson("spec_basic.json")
#print(equipmentData)
for i in equipmentData:
    equipment=equipmentData[i]
    #카혼목 api 오류 해결되면 변경할 것
    if(equipment["이름"]=="카오스 혼테일의 목걸이"):
                totalStat["max_hp_rate"]+=10
                totalStat["max_mp_rate"]+=10
    for j in equipment:
        if j=="잠재등급" or j=="에디등급":
            continue
        if j=="이름":
            setName= setCheck(equipment[j])
            if setName in equipmentSet:
                equipmentSet[setName]+=1
            continue
        if j=="잠재옵션" or j=="에디옵션":
            options=equipment[j]
            for k in options:
                if k==None:
                    continue
                print(k)
                optionName, optionAmount=k.lower().split(" : ")
                print(optionName, optionAmount)
                updateSpec(optionName, optionAmount, totalStat, ignore_monster_armor)
            continue
        if j=="소울옵션":
            option=equipment[j]
            if equipment[j]==None:
                continue
            optionName, optionAmount=option.lower().split(" : ")
            print("소울옵션", optionName, optionAmount)
            updateSpec(optionName, optionAmount, totalStat, ignore_monster_armor)
            continue
        for k in equipment[j]:
            if k=="base_equipment_level" or k=="equipment_level_decrease":
                continue
            if k=="ignore_monster_armor":
                if int(equipment[j][k])!=0:
                    ignore_monster_armor.append(int(equipment[j][k]))
            else:
                totalStat[k]+=int(equipment[j][k])
    
print(equipmentSet)
print(totalStat, ignore_monster_armor)
updateSetEffect(equipmentSet, totalStat, ignore_monster_armor)
totalStat["ignore_monster_armor"]=calcIgnoreMonstorArmor(ignore_monster_armor)
print(totalStat, ignore_monster_armor)
json_functions.makejson(totalStat, 'spec_equipment.json')
