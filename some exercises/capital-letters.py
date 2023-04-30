mystr=input()
def myfunc(sample):
    l=sample.split()

    # print(l)
    j=0
    flag=False
    for i in l:
        j=j+1
        
        i=i.replace(".","")
        i=i.replace(",","")
        if i==i.capitalize() and j!=1 and l[j-2]==l[j-2].replace(".","") and  (not i.isdigit()):
            flag=True
            print( "{}:{}".format(j,i))
    if flag==False:
        print(None)

myfunc(mystr)