l1=[23,56,75,23,67,34,23,90,45,34,78,34,56,34,89,34,90,23,23]
l2=[]
for i in range(0,len(l1)):
    cnt=l1.count(l1[i])
    if cnt > 1 :
        #print(l1[i], "is duplicate")
        if l1[i] not in l2:
            l2.append(l1[i])
print(l2)

d1={}
for i in range(0,len(l2)):
    k=l2[i]
    v=l1.count(l2[i])
    d1[k]=v
print(d1)


