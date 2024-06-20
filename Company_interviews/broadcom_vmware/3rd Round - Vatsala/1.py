l=[1,10,3,6,7,5,4,2,11,12,0]
n=7
l1=[]
l2=[]
for i in range(len(l)):
    j=i+1
    for j in range(i+1,len(l)):
        if l[i]+l[j] == n:
            l1=[l[i],l[j]]
            l2.append(l1)
print(l2)
