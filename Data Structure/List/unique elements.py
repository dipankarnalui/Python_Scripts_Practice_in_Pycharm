#Find unique elements in a list
l1=[1,2,1,3,4,5,7,6,7,8,9,3,10]
l2=[]
for e in l1:
    if l1.count(e) == 1:
        l2.append(e)
print(list(set(l2)))




