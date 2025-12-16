'''
“A decorator is a function that adds extra functionality to another function without modifying its source code.”
'''
def my_decorator(func):
    def wrapper():
        print("Before Calling function")
        func()
        print("Before Calling function")
    return wrapper

@my_decorator
def greet():
    print("Hello")

greet()

