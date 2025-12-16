'''
This is NOT a shallow copy.
This is assignment (reference copy).
'''
l1=[1,2,3]
l2=l1
print("l1=",l1)
print("l2=",l2)
l2.append(4)
print("l1=",l1)
print("l2=",l2)

