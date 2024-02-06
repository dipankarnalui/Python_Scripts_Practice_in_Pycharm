#sort of numbers
l1=[34,756,2,45,24,56]
print("input list = ", l1)
for i in range(0,len(l1)):
    j=i+1
    for k in range(j, len(l1)):
        if l1[i] > l1[k] :
            l1[i], l1[k] = l1[k], l1[i] #single line swap
print("sorted list = ",l1)