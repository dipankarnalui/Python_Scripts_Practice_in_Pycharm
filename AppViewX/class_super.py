class C1():
    def __init__(self, a, b):
        self.a=2
        self.b=b
    def display(self):
        print(a)
    def return_1(self):
        return self.a

class C2(C1):

    def __init__(self, a, b):
        super()
        self.a = a
        self.b=b

    def out1(self):
        print(a)
a=1
b=2
obj1=C2(a,b)
print(obj1.a)