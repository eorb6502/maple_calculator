def calc_force_diff(map_info, character_force):
    arcane_force, authentic_force=character_force
    if map_info["tag"]=="None":
        return 1
    elif map_info["tag"]=="arcane":
        tmp=arcane_force/map_info["force"]
        arcane_arr=[0, 0.01, 0.3, 0.5, 0.7, 1, 1.1, 1.3, 1.5]
        arcane_arr_final_damage=[0.1, 0.3, 0.6, 0.7, 0.8, 1, 1.1, 1.3, 1.5]
        for i in range(8):
            if tmp>=arcane_arr[i] and tmp<arcane_arr[i+1]:
                return arcane_arr_final_damage[i]
        return arcane_arr_final_damage[8]
    elif map_info["tag"]=="authentic":
        if map_info["force"]>=authentic_force:
            return 1-0.01*( map_info["force"]-authentic_force)
        else:
            return min(1-0.005*( map_info["force"]-authentic_force), 1.25)
    else:
        print("this should never happen")

print(calc_force_diff({"tag" : "authentic", "force" : 0}, (50, 60)))