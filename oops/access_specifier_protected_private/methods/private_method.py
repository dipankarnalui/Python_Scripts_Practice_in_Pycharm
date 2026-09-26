class A():
    def __init__(self):
        pass
    def public_method(self):
        print("public called")
    def _protected_method(self):
        print("protected called")
    def __private_method(self):
        print("private called")

obj=A()
obj.public_method()
obj._protected_method()
#obj.__private_method() #error

