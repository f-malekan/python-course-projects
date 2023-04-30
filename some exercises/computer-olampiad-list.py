tedad=int(input())
l=[]
for i in range(tedad):
    a=input()
    b=a.split(".")
    b[1]=b[1].capitalize()
    l.append(b)
l.sort(key=lambda row: (row[0], row[1]))
# print(l)
for i in l:
    print(i[0],i[1],i[2])