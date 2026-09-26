class A():
    def show(self):
        print("A")

#without super
'''
class B(A):
    def show(self):
        print("B")
'''

#with super
class B(A):
    def show(self):
        super().show()

b=B()
b.show()

