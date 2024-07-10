import json
import json_functions
import requests
"""
maple_class_arr=["히어로", "팔라딘", "다크나이트", "소울마스터", "미하일", "블래스터", "데몬슬레이어", "아란", "카이저", "아델", "제로", "핑크빈", "바이퍼", "캐논슈터", "스트라이커", "은월", "아크", "예티", "보우마스터", "신궁", "패스파인더", "윈드브레이커", "와일드헌터", "메르세데스", "카인", "캡틴", "메카닉", "엔젤릭버스터", "아크메이지(불,독)", "아크메이지(썬,콜)", "비숍", "플레임위자드", "배틀메이지", "에반", "루미너스", "일리움", "라라", "키네시스", "나이트로드", "섀도어", "듀얼블레이드", "나이트워커", "팬텀", "카데나", "칼리", "호영", "제논", "데몬어벤져"]
maple_class={
    "STR":["히어로", "팔라딘", "다크나이트", "소울마스터", "미하일", "블래스터", "데몬슬레이어", "아란", "카이저", "아델", "제로", "핑크빈", "바이퍼", "캐논슈터", "스트라이커", "은월", "아크", "예티"], \
    "DEX":["보우마스터", "신궁", "패스파인더", "윈드브레이커", "와일드헌터", "메르세데스", "카인", "캡틴", "메카닉", "엔젤릭버스터"], \
    "INT":["아크메이지(불,독)", "아크메이지(썬,콜)", "비숍", "플레임위자드", "배틀메이지", "에반", "루미너스", "일리움", "라라", "키네시스"], \
    "LUK":["나이트로드", "섀도어", "듀얼블레이드", "나이트워커", "팬텀", "카데나", "칼리", "호영", "제논"], \
    "HP":["데몬어벤져"]
}
for characterClass in maple_class_arr:
    #characterClass="칼리"
    mainStat=[]
    for i in maple_class:
        if characterClass in maple_class[i]:
            #print(i)
            mainStat.append(i)
            break
    subStat=[]
    if mainStat[0]=="STR":
        subStat.append("DEX")
    elif mainStat[0]=="DEX":
        subStat.append("STR")
    elif mainStat[0]=="LUK":
        if characterClass!="제논":
            subStat.append("DEX")
            if characterClass=="섀도어" or characterClass=="듀얼블레이드" or characterClass=="카데나":
                subStat.append("STR")
        else:
            mainStat.append("STR")
            mainStat.append("DEX")
    elif mainStat[0]=="INT":
        subStat.append("LUK")
    else:
        subStat.append("STR")
    print(characterClass, mainStat, subStat)
    """
headers = {
"x-nxopen-api-key": "test_4cf454573b36e0ef7bddfcd133597df43e86736d0e4d6b693c2928ee6b54a1dbefe8d04e6d233bd35cf2fabdeb93fb0d"
}
file_path="spec.json"
url="https://open.api.nexon.com/maplestory/v1/character/stat"
data=json_functions.openjson(file_path)
ocid="?ocid=" + data["ocid"]
urlString = url + ocid
response_stat = requests.get(urlString, headers=headers)
print(response_stat.json())