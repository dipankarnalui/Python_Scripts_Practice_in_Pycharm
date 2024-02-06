class Product:

    def __new__(cls, *args, **kwargs):
        print("new called")
        return super().__new__(cls, *args, **kwargs)

    def __init__(self):
        print("Init-called")

    def __del__(self):
        print("Dtor called")


p1 = Product()
