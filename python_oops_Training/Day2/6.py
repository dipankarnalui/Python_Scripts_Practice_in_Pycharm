# class level
class Person:
    def __init__(self, name, loc):
        self.name = name
        self.loc = loc
    def __eq__(self, other):
        print("Some body called mee......")
        if type(other) == Person:
            if self.name == other.name and self.loc == other.loc:
                return True
            else:
                return False
        return False
# SRC code level
p1 = Person("ravi", "blr")
p2 = Person("ravi2", "blr")
if p1 == p2:  # Person.__eq__(p1,p2)
    print("Same Person")
else:
    print("Diff person")