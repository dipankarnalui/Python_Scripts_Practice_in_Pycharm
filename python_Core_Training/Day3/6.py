class Person:
    # default-cum-parameterized constructor
    def __init__(self, name=None, loc=None):
        self.name = name
        self.loc = loc

    def show(self):
        print(self.name, self.loc)


# main program
p1 = Person(name="ravi", loc="blr")
p1.show()
p2 = Person()  # is it valid ?
p2.show()