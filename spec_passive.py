import json
import json_functions

maple_class={
    "str":["히어로", "팔라딘", "다크나이트", "소울마스터", "미하일", "블래스터", "데몬슬레이어", "아란", "카이저", "아델", "제로", "핑크빈", "바이퍼", "캐논슈터", "스트라이커", "은월", "아크", "예티"], \
    "dex":["보우마스터", "신궁", "패스파인더", "윈드브레이커", "와일드헌터", "메르세데스", "카인", "캡틴", "메카닉", "엔젤릭버스터"], \
    "int":["아크메이지(불,독)", "아크메이지(썬,콜)", "비숍", "플레임위자드", "배틀메이지", "에반", "루미너스", "일리움", "라라", "키네시스"], \
    "luk":["나이트로드", "섀도어", "듀얼블레이드", "나이트워커", "팬텀", "카데나", "칼리", "호영", "제논"], \
    "max_hp":["데몬어벤져"]
}

basicInfo=json_functions.openjson("spec.json")
specSkill=json_functions.openjson("passive_class.json")
characterClass=basicInfo["class"]
characterLevel=basicInfo["level"]
basicSpec=specSkill[characterClass]
print(basicSpec)
json_functions.combine_and_save_json(basicInfo, basicSpec, 'spec_basic.json')



