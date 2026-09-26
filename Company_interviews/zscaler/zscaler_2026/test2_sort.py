list1 = [1, 6, 5, 4, 9]
list2 = [2, 8, 7]

#op = [1, 2, 4, 5, 6, 7, 8, 9]

list1.extend(list2)

print(list1)

for i in range(len(list1)):
    #print(list1[i])
    for j in range(i+1,len(list1)):
        #print(list1[i])
        if list1[i]>list1[j]:
            list1[j],list1[i]=list1[i],list1[j]

print(list1)

