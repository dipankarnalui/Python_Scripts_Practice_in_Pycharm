'''
It receives the class itself (cls), not an instance (self).A class method is used when:
The method works with class-level data
The method should affect all objects of the class
The method logically belongs to the class, not to one specific object
'''

class Employee:
    company="cisco"

    #It receives the class itself (cls), not an instance (self).
    @classmethod
    def class_method(cls):
        print(cls.company)
        #print(company)
        #print(self.company)

e=Employee()
e.class_method()
