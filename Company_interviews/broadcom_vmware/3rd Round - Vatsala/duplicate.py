l1=[1,2,3,1,4,5,2] #with duplicate
print(l1)
#without using the for loop,tell me if the list has duplicate
s1=set(l1)
print(s1)
if len(s1) == len(l1):
    print("list does not have duplicate")
else:
    print("list has duplicate")