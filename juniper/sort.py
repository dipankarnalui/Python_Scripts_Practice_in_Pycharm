'''
list1=[56,36,23,45,78,90,23,56]

len1=len(list1)

for i in range(0,len1):
    #print(list1[i])
    for j in range(i+1,len1):
        #print(list1[i+1])
        if list1[i] > list1[j]:
            tmp = list1[i]
            list1[i] = list1[j]
            list1[j] = tmp
print(list1)
'''
#list1.remove(56)
#print(list1)
list1=[23, 23, 36, 45, 56, 56, 78, 90,56,56,56]
index=[]
#print(type(index))
for i in range(0, len(list1)):
    if list1[i] == 56:
        #print(i,list1[i])
        index.append(i)
print(index)
list2 = list1.copy()

cnt=list2.count(56)
for i in range(0,cnt):
    list2.remove(56)
print(list2)

'''
list1.remove(56)
print(list1)
'''