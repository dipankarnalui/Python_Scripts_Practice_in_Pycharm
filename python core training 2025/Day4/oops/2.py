class Employee:
      def __init__(self):
          self.eid=0
          self.name=None
          self.dept=None
          self.salary=0
      def setdetails(self,eid,name,dept,salary):
          self.eid=eid
          self.name=name
          self.dept=dept
          self.salary=salary
      def showdetails(self):
          print(self.eid,self.name,self.dept,self.salary)

emp1 = Employee()   # emp1=65524  (mutable data structure)
emp2 = Employee()   # emp2=45678  (mutable data structure)

emp1.showdetails()  # 

emp1.setdetails(1234,"hari","devops",85000)
#Employee.setdetails(emp1,1234,"hari","devops",85000)

emp2.setdetails(1235,"ravi","datasci",95000)

emp1.showdetails()
emp2.showdetails()

