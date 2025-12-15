l1=[1,2,3,4,5,6,7]

l2=[str(l1[i])+"even" for i in range(len(l1)) if l1[i]%2==0 ]
print(l2)

