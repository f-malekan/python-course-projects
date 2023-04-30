mylist=[]
for i in range(0,10):
    a=input()
    mylist.append(a)

countermax=0
result=0
for i in mylist:
    i=int(i)
    avvaldivisorcount=0
    for j in range(1,i+1):
        if(i%j==0):
            divisorcount=0
            for z in range(1,j):
                if(j%z==0):
                    divisorcount=divisorcount+1
            if (divisorcount==1):
                avvaldivisorcount=avvaldivisorcount+1
    if(avvaldivisorcount>countermax):
        countermax=avvaldivisorcount
        result=i
    elif(avvaldivisorcount==countermax):
        if(i>result):
            result=i

print(result,countermax)
