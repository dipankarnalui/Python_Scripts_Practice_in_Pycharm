import copy
l1=[1,2,3,4,5,6]
print("l1=",l1)
l2=copy.deepcopy(l1)
print("l1 = after deepcopy =",l1)
print("l2=",l2)

l1.append(7)
print("l1=",l1)
print("l2=",l2)

print(id(l1))
print(id(l2))


