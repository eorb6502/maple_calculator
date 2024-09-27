import json_functions
import csv

def opencsv(file_name):
    arr=[]
    with open(file_name, 'r', encoding='utf-8') as file:
        rdr=csv.reader(file)
        for idx, line in enumerate(rdr):
            if idx==0: continue
            arr.append(line)
    return arr
maple_class_arr=["히어로", "팔라딘", "다크나이트", "소울마스터", "미하일", "블래스터", "데몬슬레이어", "아란", "카이저", "아델", "제로", "핑크빈", "바이퍼", "캐논마스터", "스트라이커", "은월", "아크", "예티", "보우마스터", "신궁", "패스파인더", "윈드브레이커", "와일드헌터", "메르세데스", "카인", "캡틴", "메카닉", "엔젤릭버스터", "아크메이지(불,독)", "아크메이지(썬,콜)", "비숍", "플레임위자드", "배틀메이지", "에반", "루미너스", "일리움", "라라", "키네시스", "나이트로드", "섀도어", "듀얼블레이더", "나이트워커", "팬텀", "카데나", "칼리", "호영", "제논", "데몬어벤져"]

tmp_dict2=json_functions.openjson("./skill_db/maple_v_skills.json")
tmp_dict=json_functions.openjson("./skill_db/maple_all_skills_stats_modified.json")
for i in tmp_dict2:
    for j in tmp_dict2[i]:
        for k in tmp_dict2[i][j]:
            tmp_dict[i][j][k]=tmp_dict2[i][j][k]
print(tmp_dict)
json_functions.makejson(tmp_dict, "./skill_db/maple_skills_final.json")