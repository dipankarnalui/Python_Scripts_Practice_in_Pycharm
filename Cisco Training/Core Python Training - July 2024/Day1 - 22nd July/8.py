import os

def greet():
    print("hello")
greet()

print(os.name)
print(os.getpid())

num1=input("first : ")
num2=input("sec : ")
r = int(num1) + int(num2)
print("result",r)