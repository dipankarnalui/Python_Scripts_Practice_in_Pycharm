def add(*a):
    print(*a)
    print(a)
    print(type(a))
    sum=0
    for e in a:
        sum=sum+e
    return sum
r=add(1,2,3,4)
print(r)
