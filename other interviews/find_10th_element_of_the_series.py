#find 10th element of this series
l1=[7,10,8,11,9,12]
l2=[]
first=l1[0]
l2.append(first)
flag=True
for i in range(0,10):
    if flag is True:
        second=first+3
        flag=False
    else:
        second = first - 2
        flag = True
    l2.append(second)
    first=second
print(l2)
