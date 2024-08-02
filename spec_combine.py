import json_functions
def combine(dict1, dict2):
    for i in dict2:
        if i not in dict1:
            dict1[i]=dict2[i]
        else:
            if i=="ignore_monster_armor":
                dict1[i]=1-(1-dict1[i])*(1-dict2[i])
            elif i=="final_damage":
                dict1[i]=(1+dict1[i])*(1+dict2[i])-1
            else:
                dict1[i]+=dict2[i]
def make_spec_final():
    characterClass=json_functions.openjson("./assets/spec.json")["class"]
    specBasic=json_functions.openjson("./assets/spec_basic.json")
    specEquipment=json_functions.openjson("./assets/spec_equipment.json")
    specHAP=json_functions.openjson("./assets/spec_hyper_ability_propensity.json")
    specSkill=json_functions.openjson("./assets/spec_skills.json")
    specSymbol=json_functions.openjson("./assets/spec_symbol.json")
    specUnion=json_functions.openjson("./assets/spec_union.json")
    specTitle=json_functions.openjson("./assets/spec_title.json")
    specSet=json_functions.openjson("./assets/spec_set.json")
    specCash=json_functions.openjson("./assets/spec_cash.json")
    equipmentRawdata=json_functions.openjson("./assets/equipment.json")
    specFinal={}
    combine(specFinal, specUnion)
    combine(specFinal, specEquipment)
    combine(specFinal, specHAP)
    combine(specFinal, specSkill)
    combine(specFinal, specSymbol)
    combine(specFinal, specTitle)
    combine(specFinal, specBasic)
    combine(specFinal, specSet)
    combine(specFinal, specCash)
    if (characterClass=="히어로" or characterClass=="팔라딘" or characterClass=="소울마스터")and (equipmentRawdata["무기"]["종류"].find("한손")!=-1):
        specSkill["damage"]-=0.1
    #print(specFinal)
    json_functions.makejson(specFinal, "./assets/spec_final.json")