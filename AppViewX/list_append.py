a = [[1,2],[3,1]]
b = [[3,6],[2,9]]
c = [[5,1],[8,10]]
#Expected: [[1,2,3,6,5,1],[3,1,2,9,8,10]]
l1=[]
l2=[]
l1.append(a[0][0])
l1.append(a[0][1])
l2.append(a[1][0])
l2.append(a[1][1])
l1.append(b[0][0])
l1.append(b[0][1])
l2.append(b[1][0])
l2.append(b[1][1])
l1.append(c[0][0])
l1.append(c[0][1])
l2.append(c[1][0])
l2.append(c[1][1])
l3 =[]
l3.append(l1)
l3.append(l2)
print(l3)

