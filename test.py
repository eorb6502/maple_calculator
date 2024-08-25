import json_functions

tmp=json_functions.openjson("./db/map_db.json")
for i in tmp:
    for j in tmp[i]:
        arr=[]
        for k in tmp[i][j]:
            arr.append(k)
        print(arr)
    