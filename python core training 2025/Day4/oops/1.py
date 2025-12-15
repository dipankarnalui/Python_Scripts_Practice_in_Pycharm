class Employee:
      def __init__(self):
          self.eid=0
          self.name=None
          self.dept=None
          self.salary=0

# create rows of the TABLE
# create objects of the class/Create instances of the class
emp1 = Employee()
emp2 = Employee()

# we have eid=1234 name="hari" dept="devops" salary=85000
emp1.eid=1234
emp1.name="hari"
emp1.dept="devops"
emp1.salary=85000

emp2.eid=1235
emp2.name="ravi"
emp2.dept="datasci"
emp2.salary=95000

print(emp1.eid,emp1.name,emp1.dept,emp1.salary)
print(emp2.eid,emp2.name,emp2.dept,emp2.salary)
