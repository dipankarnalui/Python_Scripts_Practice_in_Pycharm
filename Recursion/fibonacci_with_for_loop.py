n=10
first,second=0,1
l1=[first,second]
for i in range(0,n):
    sum=first + second
    l1.append(sum)
    first,second=second,sum
print(l1)

