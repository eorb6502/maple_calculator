import requests
import json_functions

def make_spec_basic(basicData, headers):
    url="https://open.api.nexon.com"
    #basicData=json_functions.openjson("./assets/spec.json")
    id=basicData["ocid"]  #내꺼 f80bbe45dd55bbd3ceb099cf8da9398c
    characterClass, characterLevel=basicData["class"], basicData["level"]
    ocid="?ocid="+id
    get_stat = url + "/maplestory/v1/character/stat" + ocid
    ###get_propensity = url + "/maplestory/v1/character/propensity" + ocid
    response_stat=requests.get(get_stat, headers=headers).json()
    ###response_propensity=requests.get(get_propensity, headers = headers)
    ###print(response_propensity.json())
    specBasic={
        "name" : basicData["name"],
        "class" : basicData["class"],
        "level" : basicData["level"],
        "str" : 0,
        "dex" : 0,
        "luk" : 0,
        "int" : 0,
        "max_hp" : 0,
        "max_mp" : 0,
        "critical_rate":5
    }
    #print(response_stat["final_stat"])
    #데벤져 가져오기 조금 이상함
    for i in response_stat["final_stat"]:
        statValue=i["stat_value"]
        if i["stat_name"].find("AP")==-1:
            continue
        i=i["stat_name"].split()[-1].lower()
        if i not in specBasic:
            i="max_"+i
            specBasic[i]+=int(statValue)
        else:
            specBasic[i]+=int(int(statValue)*1.15)
    if characterClass=="데몬어벤져":
        specBasic["max_hp"]=90*characterLevel+545
    #print(specBasic)
    json_functions.makejson(specBasic, "./assets/spec_basic.json")
    return specBasic

"""make_spec_basic({
    "x-nxopen-api-key": "test_5d1d2bbf3be59f1d5bf961c60a1937b5f5c7d6a8133966a63f38c7ebc5bd3a08efe8d04e6d233bd35cf2fabdeb93fb0d"
    })"""