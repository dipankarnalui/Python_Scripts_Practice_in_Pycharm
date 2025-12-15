class Employee:
    def setname(self,name):
        self.name = name
    def setdept(self,dept):
        self.dept = dept
    def setsalary(self,salary):
        self.salary = salary
    def setlocation(self,loc):
        self.location = loc
    def showdetails(self):
        print("Name = ",self.name)
        print("Dept = ",self.dept)
        print("Loct = ",self.location)
        print("Salary = ",self.salary)

# main program
row1 = Employee()

row1.setname("Ajith")
row1.setdept("sales")
row1.setsalary(57000)
row1.setlocation("blr")

row1.showdetails()  # name = Ajith    
                    # dept = sales
                    # loc  = blr
                    # salary = 57000


