#Method overriding and polymorphism are related, but they are not the same.
#Method overriding is one mechanism through which runtime polymorphism is achieved.

class A():
    def show(self):
        print("A")
class B(A):
    def show(self):
        print("B")
class C(B):
    def show(self):
        print("C")

a=A()
b=B()
c=C()

a.show()
b.show()
c.show()

