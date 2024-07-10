import json
from collections import OrderedDict

def makejson(dict, name):
    with open(name, 'w', encoding="utf-8") as make_file:
        json.dump(dict, make_file, ensure_ascii=False, indent='\t')
def openjson(name):
    with open(name, 'r', encoding="utf-8") as file:
        tmp=json.load(file)
    return tmp
def combine_and_save_json(dict1, dict2, name):
    for i in dict2:
        if i in dict1:
            if i=="ignore_monster_armor":
                dict1[i]=1-(1-dict1[i])*(1-dict2[i])
            else:
                dict1[i]+=dict2[i]
        else:
            dict1[i]=dict2[i]
    #print(dict1)
    makejson(dict1, name)
