class A():
    def __init__(self,a):
        self.a=a
    def show(self):
        print("A")
        print(self.a)
class B(A):
    def __init__(self):
        super().__init__(20)
    def show(self):
        super().show()

a=A(10)
#a.show()

b=B()
b.show()
