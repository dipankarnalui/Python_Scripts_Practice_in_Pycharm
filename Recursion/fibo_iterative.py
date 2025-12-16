n=10
first,second=0,1
l1=[first,second]
count=0
print(l1)
while(count<n):
    sum=first + second
    l1.append(sum)
    print(l1)
    first,second=second,sum
    count+=1
