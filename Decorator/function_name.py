def log_decorator(func):
    def wrapper():
        print("start of ", func.__name__ )
        func()
        print("end of ", func.__name__)
    return wrapper

@log_decorator
def greet():
    print("Hello")

greet()

