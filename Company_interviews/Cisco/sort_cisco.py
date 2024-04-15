#Cisco_Interview
#Write a code to sort the elements in the list
list1=[56,23,59,12,34]
list1.sort()
print(list1)
for i in range(0,len(list1)):
    for j in range(i+1, len(list1)):
        if list1[i] > list1[j]:
            t= list1[j]
            list1[j] = list1[i]
            list1[i] = t
print(list1)

