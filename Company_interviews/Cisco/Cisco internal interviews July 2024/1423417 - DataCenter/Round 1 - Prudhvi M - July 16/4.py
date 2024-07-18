#multi Level inheri
'''
class A():
    def __init__(self,a):
        #if type(a) == int:
            self.a : str = a
        #elif self.a == int(a):
        #    self.a = a
        #else:
        #    print("param not int")

        self.b=2

    def test1(self):
        print("this is A")
class B(A):
    def __init__(self):
        super.__init__(self)
        self.c = 1
        self.d = 2
    def test2(self):
        print("this is B")
class C(B):
    def __init__(self):
        super.__init__(self)
        self.b = 1
        self.d = 2
    def test3(self):
        print("this is C")

c_obj=C(b_obj)
print(c_obj.a)

'''
