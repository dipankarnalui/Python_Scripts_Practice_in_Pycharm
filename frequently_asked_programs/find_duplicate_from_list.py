#Find duplicate elements in a list.
l1=[2,67,20,4,30,67,90,37,2,30]
l2=[]

for e in l1:
    if l1.count(e) > 1:
        #print(e)
        if e not in l2:
            l2.append(e)
print(f"duplicate elements are => {l2}",end="")

