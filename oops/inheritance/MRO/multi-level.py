class A:
    def show(self):
        print("A")


class B(A):
    def show(self):
        print("B")


class C(B):
    pass


c = C()
c.show()
print(C.mro())
