
def outer():
    print("Outer function")
    def inner():
        print("Inner function")
    inner()

outer()