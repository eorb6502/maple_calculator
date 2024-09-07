import main_function
import json_functions
import json
import uvicorn
import calc_damage
from typing import List
from fastapi import FastAPI, Query, Request
from fastapi.templating import Jinja2Templates
from datetime import datetime

api = FastAPI()
templates= Jinja2Templates(directory="templates")

@api.get("/")
def get_index(request: Request):
    return templates.TemplateResponse("test_html.html", {"request": request})

@api.get('/initialize/{characterName}')
def return_spec_final(characterName: str):
    #main_function.make_spec_final(characterName)
    now=datetime.now()
    return main_function.make_spec_final(characterName), now.strftime('%Y-%m-%d %H:%M:%S')

@api.get('/calculate/')
def calculate_dmg(final: str=None, guild_doping: str=None, mode: str = "normal", doping: List[str] = Query(None), dmg: float=0, attack_count : int=1, hyper_damage : float=0, core_reinforce : float=0, map_type : str="arcane", map_region : str="소멸의 여로", map_name : str="풍화된 기쁨의 땅", core_igm : float = 0, skill_igm : float = 0, skill_final_damage : float = 0):
    map_db=json_functions.openjson("./db/map_db.json")
    mob_db=json_functions.openjson("./db/mob_db.json")
    force=map_db[map_type][map_region][map_name]["force"] 
    mob_info=mob_db[map_db[map_type][map_region][map_name]["monster"]]
    final = json.loads(final)
    guild_doping= json.loads(guild_doping)
    #print(mob_info, force, map_type, final, guild_doping)
    old, fd = calc_damage.calc_one_line_dmg(final, guild_doping, mode, doping, dmg, attack_count, hyper_damage, core_reinforce, {
        "level" : mob_info["level"],
        "armor" : mob_info["armor"],
        "property" : mob_info["property"]
    }, {"tag" : map_type, "force" : force}, core_igm, skill_igm, skill_final_damage)
    return old, fd, mob_info["hp"]


if __name__ == "__main__":
    uvicorn.run(api, host="127.0.0.1", port=8000)