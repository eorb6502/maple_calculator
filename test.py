import json_functions

tmp=json_functions.openjson("./db/map_db.json")
for i in tmp:
    sex=[]
    for j in tmp[i]:
        arr=[]
        sex.append(j)
        for k in tmp[i][j]:
            arr.append(k)
        print(j,arr)
        print()
    