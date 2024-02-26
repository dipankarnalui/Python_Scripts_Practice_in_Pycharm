#sort the dictionary using values, not by keys
d1= {23: 3, 51: 2, 24: 5, 78: 4, 90: 1}
print("d1 = ",d1)

l2=list(d1.keys())
l3=list(d1.values())
print("l2 = ",l2)
print("l3 = ",l3)

l4=[]
for k,v in d1.items():
    l4.append((k,v))
print("l4 = ",l4)

l3.sort()
print("l3 = ",l3)
d2={}
for e in l3:
    for i in range(len(l4)):
        if e == l4[i][1]:
            k=l4[i][0]
            d2[k]=e
print("d2 = ",d2)
