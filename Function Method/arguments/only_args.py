def add_numbers(*a):
    print(a)
    print(type(a))
    total=sum(a)
    print(total)
    return total

add_numbers(1,2,3)
add_numbers(10,20,30,40)
add_numbers(10,20)
