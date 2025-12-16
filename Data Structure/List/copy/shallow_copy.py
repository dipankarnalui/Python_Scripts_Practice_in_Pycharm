'''
copy.copy() always creates a shallow copy.
If the object contains only immutable elements (such as => int), it behaves like a deep copy.
Problems appear only with nested mutable objects.
'''


import copy

l1=[1,2,3,4,5,6]
print("l1=",l1)
l2=copy.copy(l1)
l1.append(7)
print("l2=",l2)
print("l1=",l1)

print(id(l1))
print(id(l2))
