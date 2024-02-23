#sort dictionary netscope
#input list
l1=[23,51,24,78,24,45,34,24,23,78,23,51,24,78,90,78,24]
#Final output={45: 1, 34: 1, 90: 1, 51: 2, 23: 3, 78: 4, 24: 5}

#Steps:
#Form a dictionary from the input List
#key = distinct element of the input list
#value = count of distinct element
#output of dictionary =  {23: 3, 51: 2, 24: 5, 78: 4, 45: 1, 34: 1, 90: 1}
#sort the dictionary using values, not by keys
#print the sorted dictionary as final output

print("l1 = ", l1)
d1={}
for i in range(len(l1)):
    cnt=l1.count(l1[i])
    ele=l1[i]
    d1[ele]=cnt
print("d1 = ",d1)

l2=[]
l3=[]
l4=[]
for k,v in d1.items():
    #print(k,v)
    l2.append(k)
    l3.append(v)
    l4.append((k,v))
print("l2 = ",l2)
print("l3 = ",l3)
print("l4 = ",l4)
l3.sort()
print("l3 = ",l3)
d2={}
for e in l3:
    for i in range(len(l4)):
        if e == l4[i][1]:
            k1=l4[i][0]
            d2[k1]=e
print("d2 = ",d2)
