#string operations using list
x = "AAABBCCAADDV"
out = "A5B2C2D2V1"

print("Conversion string into to list")
l1=list(x)
print("l1 = ",l1)

print("remove duplicates ==>")
l2=[]
for i in range(len(l1)):
    if l1[i] not in l2:
        l2.append(l1[i])
print("l2 = ", l2)

print("count of each element ==> ")
l3=[]
for i in range(len(l2)):
    cnt=l1.count(l2[i])
    l3.append(cnt)
print("l3 = ",l3)

print("Merge nonDuplicate element and count ==>")
l4=[]
for i in range(len(l2)):
    l4.append(l2[i] + str(l3[i]))
print("l4 = ",l4)

print("Conversion list into string finally ==> ")
s1=''
for i in range(len(l4)):
    s1 = s1 + l4[i]
print("s1 = ",s1)