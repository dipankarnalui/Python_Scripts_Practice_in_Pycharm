class Person:
    def __init__(self, name, loc):
        self.name = name
        self.loc = loc

    def show(self):
        print(self.name, self.loc)


p1 = Person("ravi", "blr")
p2 = Person("ravi", "blr")
if p1 == p2:  # p1.__eq__(p2)
    # compare the address of p1 & address of p2
    print("Person Details are Equal")
else:
    print("Person Details are Unequal")