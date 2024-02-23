#duplicate
l1=[1,4,5,8,6,1,3,8,1,5,8]
d1={}
for i in range(0,len(l1)):
    cnt=l1.count(l1[i])
    if cnt > 1:
        k=l1[i]
        v=cnt
        d1[k]=v
print(d1)