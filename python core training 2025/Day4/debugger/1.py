def greet(name):
    print("HEllo",name)
    print("Hai from...")


def fun(stop):
    res=0
    for i in range(stop):
        res = res + i
    print("REsult = ",res)
    print("End of fun")


print("Main starts")
greet("Alice")
fun(100)
print("Main ends")