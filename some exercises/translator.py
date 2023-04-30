tedad=int(input())
l=[]
for i in range(tedad):
    a=input()
    b=a.split()
    l.append(b)
# print(l)

jomle=input()
jomle2=jomle.split()

translate=[]
for i in jomle2:
    flag=False
    for j in l:
        for z in j:
            if i==z:
                flag=True
                translate.append(j[0])
                break
    if flag==False:
        translate.append(i)
# print(jomle2)
# print(translate)
mystr=""
for i in translate:
    mystr=mystr+i+" "
print(mystr)
