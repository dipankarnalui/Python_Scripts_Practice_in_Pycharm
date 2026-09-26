a1 = [1,3,5,6,10,11,34,45,67,89]
a2 = [2,4,7,8,9,12,15,16]

a3=[]
i=0
j=0
while i<len(a1) and j<len(a2):
    if a1[i]<a2[j]:
        a3.append(a1[i])
        i=i+1
    else:
        a3.append(a2[j])
        j=j+1
print(a3)
