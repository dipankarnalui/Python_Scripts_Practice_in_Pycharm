@aetest.testcase
class Person(self):
    l1 = []

    @aetest.section
    def __init__(self, name, age, email, mobile):
        self.name = name
        self.age = age
        self.email = email
        self.mobile = mobile

    def add_person(self):
        l1.append(self.name, self.age, self.email, self.mobile)

    def display(self):
        if self.name in l1:
            print(self.name, self.age, self.email, self.mobile)


class Child(Person):
    pass


obj = Person("Dipankar", 30, 'abc@abc.com', 7639970299)
obj.display()

obj2 = Child()
obj2.display()