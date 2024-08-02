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

headers = {
    "x-nxopen-api-key": "test_5d1d2bbf3be59f1d5bf961c60a1937b5f5c7d6a8133966a63f38c7ebc5bd3a08efe8d04e6d233bd35cf2fabdeb93fb0d"
    }
chk=get_ocid.getocid(input(), headers)
if chk==False:
    print(chk)
else:
    spec_basic.make_spec_basic(headers)
    equipment.make_equipment_data_and_title(headers)
    spec_equipment.make_spec_equipment()
    spec_hyper_ability_propensity.make_spec_HAP(headers)
    spec_set.make_spec_set(headers)
    spec_skills.make_spec_skill(headers)
    spec_symbol.make_spec_symbol(headers)
    spec_union.make_spec_union(headers)
    spec_cash.make_spec_cash(headers)
    spec_combine.make_spec_final()
    
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