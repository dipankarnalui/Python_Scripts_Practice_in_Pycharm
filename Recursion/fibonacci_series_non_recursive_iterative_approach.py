n=10
count=0
first=0
second=1
sum=0
l1=[first,second]
print(l1)
while(count<n):
    sum=first + second
    l1.append(sum)
    print(l1)
    first=second
    second=sum
    count+=1
