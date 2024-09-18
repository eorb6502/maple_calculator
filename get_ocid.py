import requests
import json_functions
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("API_KEY")

def getocid(name, headers):
    dict={
        "name" : "",
        "ocid" : "",
        "class" : "",
        "level" : "",
        "world" : "",
        "guild" : "",
        "oguildid" : "" 
    }
    characterName = name
    print(characterName)
    urlString = "https://open.api.nexon.com/maplestory/v1/id?character_name=" + characterName
    response_id = requests.get(urlString, headers = headers).json()
    print(response_id)
    errorCode=0
    if "error" in response_id:
        return 1, {}
    urlString = "https://open.api.nexon.com/maplestory/v1/character/basic?ocid=" + response_id["ocid"]
    response_basic = requests.get(urlString, headers=headers).json()
    print(response_basic)
    if "error" in response_basic:
        return 2, {}
    dict["name"]=characterName
    dict["ocid"]=response_id["ocid"]
    dict["class"]=response_basic["character_class"]
    dict["level"]=response_basic["character_level"]
    dict["world"]=response_basic["world_name"]
    dict["guild"]=response_basic["character_guild_name"]
    if dict["guild"]!=None:
        url="https://open.api.nexon.com/maplestory/v1/guild/id?guild_name="+response_basic["character_guild_name"] + "&world_name=" + response_basic["world_name"]
        print(url)
        get_guild=requests.get(url, headers=headers).json()
        print(get_guild)
        dict["oguildid"]=get_guild["oguild_id"]
    json_functions.makejson(dict, "./assets/spec.json")
    return errorCode, dict
    
"""headers = {
    "x-nxopen-api-key": api_key
    }
getocid("따랑햄", headers)"""
