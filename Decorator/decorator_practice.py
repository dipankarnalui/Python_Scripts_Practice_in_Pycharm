def test_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@test_decorator
def greet():
    print("Hello")

greet()

