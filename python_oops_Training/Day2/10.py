class Person:
    count = 0

    def __init__(self):
        Person.count += 1

    def __del__(self):
        Person.count -= 1

    @classmethod
    def show(cls):
        print("Count = ", cls.count)


Person.show()
p1 = Person()
p2 = Person()
Person.show()
p3 = Person()
Person.show()
del p1
Person.show()





