import json
import requests
import json_functions
import get_data

headers = {
"x-nxopen-api-key": "test_4cf454573b36e0ef7bddfcd133597df43e86736d0e4d6b693c2928ee6b54a1dbefe8d04e6d233bd35cf2fabdeb93fb0d"
}
file_path="spec.json"
url="https://open.api.nexon.com/maplestory/v1/character/item-equipment"
data=json_functions.openjson(file_path)
ocid="?ocid=" + data["ocid"]
urlString = url + ocid
response_equip = requests.get(urlString, headers=headers)
equipmentDict={}
for i in response_equip.json()["item_equipment"]:
    equipmentDict[i["item_equipment_slot"]]={
        "이름" : i["item_name"], \
        "기본" : i["item_base_option"], \
        "추옵" : i["item_add_option"], \
        "강화" : i["item_etc_option"], \
        "스타포스" : i["item_starforce_option"], \
        "익셉셔널" : i["item_exceptional_option"], \
        "잠재등급" : i["potential_option_grade"], \
        "잠재옵션" : [i["potential_option_1"], i["potential_option_2"], i["potential_option_3"]], \
        "에디등급" : i["additional_potential_option_grade"], \
        "에디옵션" : [i["additional_potential_option_1"], i["additional_potential_option_2"], i["additional_potential_option_3"]], \
        "소울옵션" : i["soul_option"]
        
        }
json_functions.makejson(equipmentDict, "equipment.json")


