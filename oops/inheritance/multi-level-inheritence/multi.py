class A():
    def __init__(self):
        print("A is called")
    def method_A(self):
        print("method_A")

class B(A):
    def __init__(self):
        print("B is called")
    def method_B(self):
        print("method_B")

class C(B):
    def __init__(self):
        print("C is called")
    def method_C(self):
        print("method_C")

a=A()
a.method_A()
#a.method_B()
#a.method_C()


b=B()
b.method_A()
b.method_B()
#b.method_C()

c=C()
c.method_A()
c.method_B()
c.method_C()
