'''
Demo1:-
========
def fun():
    num = 80   # any variable defined inside fn - LOCAL VARIABLE
    print("In Fun num = ",num)


num=50       # any variable defined outside fn - Global Variables
print("Main")
fun()
print("In Main num = ",num)


output:-
--------
Main
In Fun num = 80
In Main num = 50


Demo2:-
========
def fun():
    print("In Fun num = ",num)


num=50       # any variable defined outside fn - Global Variables
print("Main")
fun()
print("In Main num = ",num)

output:-
--------
Main
In Fun num = 50
In Main num = 50



Demo3:-
========
def fun():
    global num  # here after "num" is a GLOBAL VARIABLE
    num = 20
    print("In Fun num = ",num)


num=50       # any variable defined outside fn - Global Variables
print("Main")
print("In Main num = ",num)
fun()
print("In Main num = ",num)

output:-
--------
Main
In Main num = 50
In Fun num = 20
In Main num = 20

'''