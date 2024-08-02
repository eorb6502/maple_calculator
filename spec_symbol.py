import json
import json_functions
import requests

def make_spec_symbol(headers):
    spec={
        "str_wo_rate" : 0,
        "dex_wo_rate" : 0,
        "int_wo_rate" : 0,
        "luk_wo_rate" : 0,
        "max_hp_wo_rate" : 0,
        "arcane_force" : 0,
        "authentic_force" : 0,
    }
    url="https://open.api.nexon.com/maplestory/v1/character/"
    data=json_functions.openjson("./assets/spec.json")
    ocid="?ocid=" + data["ocid"]
    characterLevel=data["level"]
    urlString = url + "symbol-equipment" +ocid
    response_symbol= requests.get(urlString, headers=headers).json()
    for i in response_symbol["symbol"]:
        if i["symbol_name"].split(" : ")[0]=="아케인심볼":
            spec["arcane_force"]+=int(i["symbol_force"])
        elif i["symbol_name"].split(" : ")[0]=="어센틱심볼":
            spec["authentic_force"]+=int(i["symbol_force"])
        else:
            print("this shouldn't happen")
        spec["str_wo_rate"]+=int(i["symbol_str"])
        spec["dex_wo_rate"]+=int(i["symbol_dex"])
        spec["luk_wo_rate"]+=int(i["symbol_luk"])
        spec["int_wo_rate"]+=int(i["symbol_int"])
        spec["max_hp_wo_rate"]+=int(i["symbol_hp"])
    json_functions.makejson(spec, "./assets/spec_symbol.json")