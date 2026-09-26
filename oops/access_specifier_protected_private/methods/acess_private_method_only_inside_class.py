class A():
    def __init__(self):
        pass

    def __private_method(self):
        print("private called")
    def access_private_using_public_method(self):
        print("using the public method")
        self.__private_method()

obj=A()

#obj.__private_method() #error

##call the private method using public method and self
obj.access_private_using_public_method()

