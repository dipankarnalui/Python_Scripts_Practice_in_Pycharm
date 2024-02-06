s="abcd"
list1=[]
for i in s:
    list1.append(i)
#print(list1)

len=len(list1)
for i in range(0,len):
    for j in range(i+1, len):
        print(list1[i])

