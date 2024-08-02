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
def opencsv(file_name):
    arr=[]
    with open(file_name, 'r', encoding='utf-8') as file:
        rdr=csv.reader(file)
        for line in rdr:
            arr.append(line)
    return arr
ms_job=opencsv('ms_job_modified.csv')[1:]
ms_job_dict={}
maple_skill_dict={}
maple_skills_final={}
maple_skills={}
for i in maple_class_arr:
    maple_skill_dict[i]={
        "1" : {},
        "1.5" : {},
        "2" : {},
        "2.5" : {},
        "3" : {},
        "4" : {},
        "hyper" : {},
        "6" : {}
    }
    maple_skills_final[i]={
        "1" : {},
        "1.5" : {},
        "2" : {},
        "2.5" : {},
        "3" : {},
        "4" : {},
        "hyper" : {},
        "6" : {}
    }
for i in ms_job:
    ms_job_dict[i[0]]=i[1]
#print(maple_skills_final)
ms_job_id_dict={}
with open('ms_skill.csv', 'r', encoding='utf-8') as file:
    rdr=csv.reader(file)
    for line in rdr:
        if line[5]=="FALSE" and line[0] in ms_job_dict:
            #print(line)
            job_name, job_degree = ms_job_dict[line[0]].split()
            if float(job_degree)<6:
                maple_skills[line[2]]=job_name
            if job_name not in maple_class_arr:
                for i in maple_common_class[job_name]:
                    maple_skill_dict[i][job_degree][line[1]]=line[2]
                    maple_skills_final[i][job_degree][line[2]]={}
                ms_job_id_dict[line[1]]=job_name+"^&*"+job_degree+"^&*"+line[2]
            else:
                if line[6]=="0":
                    maple_skill_dict[job_name][job_degree][line[1]]=line[2]
                    maple_skills_final[job_name][job_degree][line[2]]={}
                    ms_job_id_dict[line[1]]=job_name+"^&*"+job_degree+"^&*"+line[2]
                else:
                    maple_skill_dict[job_name]["hyper"][line[1]]=line[2]
                    maple_skills_final[job_name]["hyper"][line[2]]={}
                    ms_job_id_dict[line[1]]=job_name+"^&*hyper^&*"+ line[2]
print(maple_skills)
#json_functions.makejson(maple_skills,"class_maple_skills.json")
#print(ms_job_id_dict)
#json_functions.makejson(maple_skill_dict, "maple_skills.json")
#print(ms_job_id_dict)
pass_arr=["updatableTime", "hpRCon","mpRCon", "time", "ppCon","ppRecovery","forceCon", "hpCon", "cooltime", "mpCon", "mobCount", "maxUseCountInOneJump", "range", "attackDelay", "damAbsorbShieldR", "stanceProp", "psdJump", "psdSpeed", "speedMax", "lv2mhp", "ballDelay", "ballDelay1","ballDelay2","ballDelay3","ballDelay4"]
with open('ms_skillCommon.csv', 'r', encoding='utf-8') as file:
    rdr=csv.reader(file)
    for idx, line in enumerate(rdr):
        if line[1] in pass_arr:
            continue
        if line[0] not in ms_job_id_dict:
            continue
        #print(ms_job_id_dict[line[0]])
        job_name, job_degree, skill_name = ms_job_id_dict[line[0]].split("^&*")
        if job_name not in maple_class_arr:
            for i in maple_common_class[job_name]:
                maple_skills_final[i][job_degree][skill_name][line[1]]=line[2]
        else:
            maple_skills_final[job_name][job_degree][skill_name][line[1]]=line[2]
#print(maple_skills_final)
#json_functions.makejson(maple_skills_final, "maple_skills_stats_modified.json")
        
