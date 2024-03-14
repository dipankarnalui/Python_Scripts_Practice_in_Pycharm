class Person():
    l1 = []

    def __init__(self, name, age, email, mobile):
        self.name = name
        self.age = age
        self.email = email
        self.mobile = mobile

    def add_person(self):
        self.l1.append(self.name, self.age, self.email, self.mobile)

    def display(self):
        print(self.name, self.age, self.email, self.mobile)


class Child(Person):
    pass


#obj1 = Person("Nirmal", 60, 'nirmal@gmail.com', 9733733286)
#obj1.display()

obj2 = Child("Dipankar", 30, 'dipankar@gmail.com', 7639970299)
obj2.display()