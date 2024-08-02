import json_functions
maple_class_arr=["히어로", "팔라딘", "다크나이트", "소울마스터", "미하일", "블래스터", "데몬슬레이어", "아란", "카이저", "아델", "제로", "핑크빈", "바이퍼", "캐논슈터", "스트라이커", "은월", "아크", "예티", "보우마스터", "신궁", "패스파인더", "윈드브레이커", "와일드헌터", "메르세데스", "카인", "캡틴", "메카닉", "엔젤릭버스터", "아크메이지(불,독)", "아크메이지(썬,콜)", "비숍", "플레임위자드", "배틀메이지", "에반", "루미너스", "일리움", "라라", "키네시스", "나이트로드", "섀도어", "듀얼블레이드", "나이트워커", "팬텀", "카데나", "칼리", "호영", "제논", "데몬어벤져"]
dict={
    "weapon_multiplier" : 0,\
    "proficiency" : 0,\
    "str" : 0,\
    "dex" : 0,\
    "int" : 0,\
    "luk" : 0,\
    "attack_power" : 0,\
    "magic_power" : 0,\
    "damage" : 0,\
    "boss_damage" : 0,\
    "final_damage" : 0,\
    "ignore_monster_armor" : 0,\
    "property" : 0,\
    "armor" : 0,\
    "critical_rate" : 0,\
    "critical_damage" : 0,\
    "max_hp" : 0,\
    "max_hp_rate" : 0,\
    "max_mp" : 0,\
    "max_mp_rate" : 0,\
}
maple_class_dict={}
for i in maple_class_arr:
    maple_class_dict[i]=dict.copy()
khali=maple_class_dict["칼리"]
khali["weapon_multiplier"]=1.3
khali["proficiency"]=0.9
khali["str"] =0
khali["dex"] =0
khali["int"] =0
khali["luk"] =60
khali["attack_power"] =120
khali["magic_power"]=0
khali["damage"]=5
khali["boss_damage"]=30
khali["final_damage"]=0.625
khali["ignore_monster_armor"]=0.36
khali["property"]=0
khali["armor"]=150
khali["critical_rate"]=40
khali["critical_damage"]=28
khali["max_hp"]=500
khali["max_hp_rate"]=15
khali["max_mp"]=500
khali["max_mp_rate"]=15
print(maple_class_dict["칼리"])
json_functions.makejson(maple_class_dict, "passive_class.json")
#아델은 패이스 제외하고 반영
#호영은 괴이봉인 제외하고 반영


