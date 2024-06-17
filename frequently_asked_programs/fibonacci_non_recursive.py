n=int(input("Enter the length : "))
print("Fibonacci series upto {}".format(n))

first=0
second=1
count=0
print(first,second, end=" ")
while count<=n-2:
    count=count+1
    third=first+second
    print(third, end=" ")
    first = second
    second = third
