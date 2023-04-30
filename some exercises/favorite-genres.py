tedad=int(input())
mylist=[]
for i in range(0,tedad):
    a=input()
    b=a.split()
    mylist.append(b)

Action=0
Comedy=0
History=0
Horror=0
Romance=0
Adventure=0
for i in mylist:
    for j in i:
        if(j=="Action"):
            Action=Action+1
        if(j=="Comedy"):
            Comedy=Comedy+1
        if(j=="History"):
            History=History+1
        if(j=="Horror"):
            Horror=Horror+1
        if(j=="Romance"):
            Romance=Romance+1
        if(j=="Adventure"):
            Adventure=Adventure+1
Mydict={"Action":Action,"Comedy":Comedy,"History":History,"Horror":Horror,"Romance":Romance,"Adventure":Adventure}
dict(sorted(Mydict.items(), key=lambda x: (x[1],x[0]), reverse=True))
for x in Mydict:
    print(x,":",Mydict[x])
