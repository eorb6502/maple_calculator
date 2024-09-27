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

def make_spec_final(str, combat_flag, preset_flags):
    equipment_flag, hyperstat_flag, ability_flag, union_flag, link_flag = preset_flags
    print(equipment_flag, hyperstat_flag, ability_flag, union_flag, link_flag)
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
        print("------basic------")
        specBasic=spec_basic.make_spec_basic(spec, headers, combat_flag)
        equipmentDict, specTitle = equipment.make_equipment_data_and_title(spec, headers, equipment_flag)
        specEquipment=spec_equipment.make_spec_equipment(equipmentDict, spec)
        specHAP = spec_hyper_ability_propensity.make_spec_HAP(spec, headers, hyperstat_flag, ability_flag)
        print("------set------")
        specSet= spec_set.make_spec_set(spec, headers)
        print("------skill------")
        guild_doping, specSkill, yanus_dict, fountain_dict = spec_skills.make_spec_skill(spec, specSet, specEquipment, equipmentDict, headers, combat_flag, link_flag)
        print("------symbol------")
        specSymbol = spec_symbol.make_spec_symbol(spec, headers)
        print("------union------")
        specUnion = spec_union.make_spec_union(spec, headers, union_flag)
        print("------cash------")
        specCash = spec_cash.make_spec_cash(spec, headers)
        specFinal = spec_combine.make_spec_final(spec, specBasic, specEquipment, specHAP, specSkill, specSymbol, specUnion, specTitle, specSet, specCash, equipmentDict)
        return guild_doping, specFinal, yanus_dict, fountain_dict, ""

#make_spec_final("츠데구")