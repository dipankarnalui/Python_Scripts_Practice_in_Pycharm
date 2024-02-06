#print reverse using slicing
l1=[10,6,3,20,5,30,5,7]
print(l1[::-1])

#Another way to do list reverse without using built in function
l2=[]
for i in range(len(l1)-1, -1, -1):
    #print(i)
    #print(l1[i])
    l2.append(l1[i])
print(l2)

#copy the content of the list to tanother list
l3=l1.copy()
l3.reverse()
print(l3)