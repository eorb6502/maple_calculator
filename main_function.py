import get_ocid
import spec_basic
import equipment
import spec_equipment
import spec_hyper_ability_propensity
import spec_set
import spec_skills
import spec_symbol
import spec_union
import spec_cash
import spec_combine
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("API_KEY")

def make_spec_final(str, combat_flag):
    headers = {
        "x-nxopen-api-key": api_key
        }
    chk, spec=get_ocid.getocid(str, headers)
    if chk!=0:
        if chk==1:
            return {}, {}, "존재하지 않는 닉네임"
        else:
            return {}, {}, "API로 데이터를 불러올 수 없는 닉네임 (장기간 미접속 등)"
    else:
        specBasic=spec_basic.make_spec_basic(spec, headers, combat_flag)
        equipmentDict, specTitle = equipment.make_equipment_data_and_title(spec, headers)
        specEquipment=spec_equipment.make_spec_equipment(equipmentDict, spec)
        specHAP = spec_hyper_ability_propensity.make_spec_HAP(spec, headers)
        specSet= spec_set.make_spec_set(spec, headers)
        guild_doping, specSkill = spec_skills.make_spec_skill(spec, specSet, specEquipment, equipmentDict, headers, combat_flag)
        specSymbol = spec_symbol.make_spec_symbol(spec, headers)
        specUnion = spec_union.make_spec_union(spec, headers)
        specCash = spec_cash.make_spec_cash(spec, headers)
        specFinal = spec_combine.make_spec_final(spec, specBasic, specEquipment, specHAP, specSkill, specSymbol, specUnion, specTitle, specSet, specCash, equipmentDict)
        return guild_doping, specFinal, ""
        
"""
import requests
import json_functions
ocid=json_functions.openjson("./assets/spec.json")["ocid"]
headers = {
    "x-nxopen-api-key": "test_4cf454573b36e0ef7bddfcd133597df43e86736d0e4d6b693c2928ee6b54a1dbefe8d04e6d233bd35cf2fabdeb93fb0d"
    }
url="https://open.api.nexon.com/maplestory/v1/character/stat?ocid="+ocid
test=requests.get(url, headers=headers).json()
for i in test["final_stat"]:
    print(i)"""
#make_spec_final("츠데구")