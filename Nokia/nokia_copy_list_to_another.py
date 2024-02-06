l1=[1,2,3,4,5]
l2=l1 #This will point to the same list having same memory address
l2=l1.copy() #This will have two different memory address
#print(id(l1))
#print(id(l2))
l2.append(6)
print(l1)
print(l2)

