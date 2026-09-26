def my_decorator(fun):
    def wrapper():
        print("execute pre-condition")
        fun()
        print("execute post-condition")
    return wrapper   #similar to property method, just like variable

@my_decorator
def greet():
    print("hi")
greet()


