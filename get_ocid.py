import requests
import json_functions

headers = {
"x-nxopen-api-key": "test_4cf454573b36e0ef7bddfcd133597df43e86736d0e4d6b693c2928ee6b54a1dbefe8d04e6d233bd35cf2fabdeb93fb0d"
}

characterName = "츠데구"
urlString = "https://open.api.nexon.com/maplestory/v1/id?character_name=" + characterName
response_id = requests.get(urlString, headers = headers)
urlString = "https://open.api.nexon.com/maplestory/v1/character/basic?ocid=" + response_id.json()["ocid"]
response_basic = requests.get(urlString, headers=headers)
print(response_id.json())
dict={"name" : characterName, "ocid" : response_id.json()["ocid"], "class":response_basic.json()["character_class"], "level": response_basic.json()["character_level"]}
json_functions.makejson(dict, "spec.json")