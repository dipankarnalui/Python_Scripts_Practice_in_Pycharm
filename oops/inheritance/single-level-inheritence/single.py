class A():
    def __init__(self):
        print("A is called")
    def method1(self):
        print("method1")

class B(A):
    def __init__(self):
        print("B is called")
    def method2(self):
        print("method2")

a=A()
a.method1()

b=B()
b.method2()
b.method1()

#a.method2() #error
