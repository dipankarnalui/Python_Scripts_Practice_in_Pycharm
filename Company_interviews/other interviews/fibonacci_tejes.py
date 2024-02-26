#0,1,1,2,3,5,

num=int(input("Enter a num: "))
first=0
second=1
i=0
print(first, end=" ")
print(second, end=" ")
while  i != num:
    #print("first= ", first, "second= ", second)
    third = first + second
    #print("third= ", third)
    print(third, end=" ")
    first = second
    second = third
    i = i + 1




