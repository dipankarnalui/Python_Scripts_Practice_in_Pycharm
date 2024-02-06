class Test:
    def __init__(self,a):
        self.a=a
    def method1(self):
        self.c = self.a + 2
    def method2(self):
        self.f = self.c + 3 #f is instance variable
        print("self.a = ", self.a)
        print("self.c = ", self.c)
        print("self.f = ", self.f)
a=5
ob=Test(a)
ob.method1()
ob.method2()
