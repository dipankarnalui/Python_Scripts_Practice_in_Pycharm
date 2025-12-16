n=10
first,second=0,1
count=0
l1=[]
while(count<n):
    l1.append(first)
    first,second=second,first + second
    count+=1
print(l1)