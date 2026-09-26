class A():
    def __init__(self):
        print("A is called")
    def method_A(self):
        print("method_A")

class B(A):#single-level
    def __init__(self):
        print("B is called")
    def method_B(self):
        print("method_B")

class C(B):#multi-level
    def __init__(self):
        print("C is called")
    def method_C(self):
        print("method_C")

class D():
    def __init__(self):
        print("D is called")
    def method_D(self):
        print("method_D")

class E(C,D):#multiple
    def __init__(self):
        print("D is called")
    def method_D(self):
        print("method_D")