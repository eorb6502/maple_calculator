import math
def d(x):
    return int(x)
def u(x):
    return int(x+1)
def logcheck(str):
    while str.find("log")!=-1:
        tmp=str[str.find("log"):]
        left=tmp.find("(")
        right=tmp.find(")")
        string=tmp[:right+1]
        deg=tmp[3:left]
        num=tmp[left+1:right]
        print(string, deg, num)
        rep="int(math.Log(" + num + "," + deg+"))"
        str = str.replace(string, rep, 1)
    str=str.lower()
    return str
x=20
str=logcheck("(1+(10+d(x/2))/100)*(1+(2*x+10)/100)-1")
print(str)
print(eval(str))