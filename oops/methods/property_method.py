class Employee:
    def __init__(self, salary):
        self._salary = salary

    @property
    def get_salary(self):
        return self._salary

e = Employee(50000)
print(e.get_salary) #not using get_salary()

#It allows a method to be accessed like an attribute/variable.

