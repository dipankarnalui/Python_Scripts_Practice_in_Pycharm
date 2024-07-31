class Employee():
    def setname(self,name):
        self.name = name

    def showname(self):
        print("Name = ",self.name)

#we have to create objects of this class
e1 = Employee() # created an object of Employee class
e2 = Employee() # created an object of Employee class

e1.name = "arun" # e1.setname("arun")
e2.name = "hari" # e1.setname("hari")

e1.showname()
e2.showname()

