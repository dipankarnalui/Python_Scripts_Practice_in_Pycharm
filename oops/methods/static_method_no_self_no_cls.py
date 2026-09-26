class A():
    @staticmethod
    def method1(): #no self, no cls
        print("no self, no cls")

a=A()
a.method1()