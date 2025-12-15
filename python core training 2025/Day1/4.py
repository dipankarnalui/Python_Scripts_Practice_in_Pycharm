import os     # all the import statements / loading library
              # should be at the start

def greet():  # define all the functions or classes
   print("Hello everybody!")

# whatever we type here is considered as main program
# left aligned 

greet()
print("OS name = ",os.name)
print("PID     = ",os.getpid())
num1 = input("Enter first  : ")
num2 = input("Enter second : ")
res = num1 + num2
print("Result",res)
