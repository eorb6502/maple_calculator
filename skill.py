import json
import json_functions
import requests

headers = {
"x-nxopen-api-key": "test_4cf454573b36e0ef7bddfcd133597df43e86736d0e4d6b693c2928ee6b54a1dbefe8d04e6d233bd35cf2fabdeb93fb0d"
}
ocid=json_functions.openjson("spec.json")["ocid"]
url="https://open.api.nexon.com/maplestory/v1/character/skill?ocid="+ocid+"&character_skill_grade="+"1.5"
get_skill=requests.get(url, headers=headers).json()
#print(get_skill)
for i in get_skill["character_skill"]:
    print(i)
    print("\n")