import requests
import json_functions
def returnStatValue(m_class, charClass):
    mainStat=[]
    for i in m_class:
        if charClass in m_class[i]:
            #print(i)
            mainStat.append(i)
            break
    subStat=[]
    if mainStat[0]=="STR":
        subStat.append("DEX")
    elif mainStat[0]=="DEX":
        subStat.append("STR")
    elif mainStat[0]=="LUK":
        if charClass!="제논":
            subStat.append("DEX")
            if charClass=="섀도어" or charClass=="듀얼블레이드" or charClass=="카데나":
                subStat.append("STR")
        else:
            mainStat.append("STR")
            mainStat.append("DEX")
    elif mainStat[0]=="INT":
        subStat.append("LUK")
    else:
        subStat.append("STR")
    return (mainStat, subStat)


maple_class={
    "STR":["히어로", "팔라딘", "다크나이트", "소울마스터", "미하일", "블래스터", "데몬슬레이어", "아란", "카이저", "아델", "제로", "핑크빈", "바이퍼", "캐논슈터", "스트라이커", "은월", "아크", "예티"], \
    "DEX":["보우마스터", "신궁", "패스파인더", "윈드브레이커", "와일드헌터", "메르세데스", "카인", "캡틴", "메카닉", "엔젤릭버스터"], \
    "INT":["아크메이지(불,독)", "아크메이지(썬,콜)", "비숍", "플레임위자드", "배틀메이지", "에반", "루미너스", "일리움", "라라", "키네시스"], \
    "LUK":["나이트로드", "섀도어", "듀얼블레이드", "나이트워커", "팬텀", "카데나", "칼리", "호영", "제논"], \
    "HP":["데몬어벤져"]
}
headers = {
"x-nxopen-api-key": "test_4cf454573b36e0ef7bddfcd133597df43e86736d0e4d6b693c2928ee6b54a1dbefe8d04e6d233bd35cf2fabdeb93fb0d"
}
url="https://open.api.nexon.com"
id="f80bbe45dd55bbd3ceb099cf8da9398c"   #내꺼 f80bbe45dd55bbd3ceb099cf8da9398c
ocid="?ocid="+id
print(ocid)
get_basic = url + "/maplestory/v1/character/basic" + ocid
get_stat = url + "/maplestory/v1/character/stat" + ocid
###get_propensity = url + "/maplestory/v1/character/propensity" + ocid
response_basic=requests.get(get_basic, headers=headers)
response_stat=requests.get(get_stat, headers=headers)
###response_propensity=requests.get(get_propensity, headers = headers)
print(response_basic.json())
print(response_stat.json())
###print(response_propensity.json())
characterClass=response_basic.json()["character_class"]
statDict={}
for i in response_stat.json()['final_stat']:
    print(i)
    statDict[i['stat_name']]=i['stat_value']
print(statDict)
mainStat, subStat = returnStatValue(maple_class, characterClass)
print(mainStat, subStat)
main=0
sub=0
for i in mainStat:
    main+=int(statDict[i])
for i in subStat:
    sub+=int(statDict[i])
print(main, sub)