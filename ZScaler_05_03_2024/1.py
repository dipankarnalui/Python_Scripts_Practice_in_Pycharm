a1 = [1,3,5,6,10,11,34,45,67,89]
a2 = [2,4,7,8,9,12,15,16]
#a3 = [1,2,3,4,5,6,7,8,9,10]
a3=[]
l1=len(a1)
l2=len(a2)
if l1<l2:
    l=l1
elif l2<l1:
    l=l2
elif l1==l2:
    l=l1
for i in range(l):
    if a1[i] < a2[i]:
        a3.append(a1[i])
        a3.append(a2[i])
    else:
        a3.append(a2[i])
        a3.append(a1[i])
if l1>l2:
    for i in range(l,l1):
        a3.append(a1[i])
elif l2>l1:
    for i in range(l,l2):
        a3.append(a2[i])
print(a3)
