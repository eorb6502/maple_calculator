import csv
import json_functions
maple_class_arr=["히어로", "팔라딘", "다크나이트", "소울마스터", "미하일", "블래스터", "데몬슬레이어", "아란", "카이저", "아델", "제로", "핑크빈", "바이퍼", "캐논마스터", "스트라이커", "은월", "아크", "예티", "보우마스터", "신궁", "패스파인더", "윈드브레이커", "와일드헌터", "메르세데스", "카인", "캡틴", "메카닉", "엔젤릭버스터", "아크메이지(불,독)", "아크메이지(썬,콜)", "비숍", "플레임위자드", "배틀메이지", "에반", "루미너스", "일리움", "라라", "키네시스", "나이트로드", "섀도어", "듀얼블레이드", "나이트워커", "팬텀", "카데나", "칼리", "호영", "제논", "데몬어벤져"]
maple_common_class={
    "모험가전사" : ["히어로", "팔라딘", "다크나이트"],
    "모험가법사" : ["아크메이지(불,독)", "아크메이지(썬,콜)", "비숍"],
    "모험가궁수" : ["보우마스터", "신궁"],
    "모험가해적" : ["캡틴", "바이퍼"],
    "모험가도적" : ["섀도어", "듀얼블레이드", "나이트로드"]
}
maple_skills=json_functions.openjson("maple_v_skills.json")
nameDict=json_functions.openjson("maple_v_skill_names.json")
maple_effects=[]
with open('ms_skillCommon.csv', 'r', encoding='utf-8') as file:
    rdr=csv.reader(file)
    for line in rdr:
        if line[2].find("log70")!=-1:
            continue
        maple_effects.append(line)
print(len(maple_effects))
maple_skills_dict={}
#print(maple_skills)
cnt=0
with open('ms_skill.csv', 'r', encoding='utf-8') as file:
    rdr=csv.reader(file)
    for line in rdr:
        if line[0]!='50000' or line[5]!="FALSE" :
            continue
        if line[1]=='500001002':
            continue
        maple_skills_dict[line[2]]=line[1]
        tmp={}
        for i in maple_effects:
            if i[0]==line[1]:
                tmp[i[1]]=i[2]
        print(tmp)
        if cnt==0:
            for i in maple_class_arr:
                maple_skills[i]["6"][line[2]]=tmp
            cnt+=1
            continue
        nameArr=line[2].split(" 강화")[0].split("/")
        #print(nameArr)
        for i in nameArr:
            job=nameDict[i]
            maple_skills[job]["6"][i]=tmp
        cnt+=1
#print(maple_skills)
#json_functions.makejson(maple_skills, "maple_v_skills.json")