class Person:

    def fun1(self):
        pass

    @staticmethod
    def fun2():
        pass

    @classmethod
    def show(cls):
        print("Count = ", cls.count)


p1 = Person()
print(p1.fun1)
print(Person.fun2)
print(p1.show)