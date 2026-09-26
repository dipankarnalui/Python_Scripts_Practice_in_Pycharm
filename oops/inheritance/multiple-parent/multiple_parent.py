class A():
    def __init__(self):
        print("A is called")
        self.x=1
    def method_A(self):
        print("method_A")

class B():
    def __init__(self):
        print("B is called")
        self.y=2
    def method_B(self):
        print("method_B")

class C(A,B):
    def __init__(self):
        print("C is called")
        self.z=3
    def method_C(self):
        print("method_C")


a=A()
a.method_A()
print(a.x)
#print(a.y) #error
#print(a.z) #error

b=B()
#b.method_A() #error
b.method_B()
#print(b.x) #error
print(b.y)
#print(b.z) #error


c=C()
c.method_A()
c.method_B()
c.method_C()

#print(c.x) #error
#print(c.y) #error
print(c.z)

