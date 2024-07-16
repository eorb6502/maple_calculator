import math
f=open("spec.txt", 'r')
arr={}
while True:
    l=f.readline().strip()
    if not l:
        break
    l=l.split()
    arr[l[0]]=float(l[1])
print(arr)
stat=(arr["main"]*4+arr["sub"])/100
attk=arr["attk"]
attk_percentage=1+arr["attk_perc"]
dmg=1+arr["dmg"]
fin_dmg=(1+arr["fin_dmg"]) * (1+arr["core"]) *1.15
weapon_const=arr["weap_const"]
proficiency=(1+arr["prof"])/2
skill=arr["skill"]
crit=1+arr["crit_per"]*(0.35+arr["crit_dmg"])
defence = 1-0.1*((1-arr["def"])*(1-0.2))
print((1-arr["def"])*(1-0.2), defence)
property=1-0*(1-arr["prop"])
print(stat, attk, dmg, dmg+arr["boss"], fin_dmg, weapon_const, proficiency, skill, crit)
print(stat*math.floor(attk*attk_percentage)*weapon_const*dmg*fin_dmg/dmg*(dmg+arr["boss"])*proficiency*skill*defence*crit*arr["level"]*property)
print(stat*attk*dmg*fin_dmg*weapon_const*proficiency*skill*crit*arr["level"]*defence)
f.close()