class Parent:
    def show(self):
        print("Parent")


class Child(Parent):
    def show(self):
        print("Child")


obj = Child()
obj.show()