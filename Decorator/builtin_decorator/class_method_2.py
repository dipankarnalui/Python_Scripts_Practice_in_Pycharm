#normal instance method ==>
class Employee:
    company="cisco"
    def normal_instance_method_with_self(self):
        self.company="comcast"
        print(self.company)
e1=Employee()
print(e1.company)
e1.normal_instance_method_with_self()
print(e1.company)


#class method =>
class Student():
    name="dipankar"
    @classmethod
    def class_method(cls):
        print(cls.name)
    def normal_method(self):
        print(self.name)
    def change_name(self):
        self.name="nalui"
s1=Student()
s1.normal_method()
print(s1.name)
s1.class_method()
s1.change_name()
print(s1.name)


