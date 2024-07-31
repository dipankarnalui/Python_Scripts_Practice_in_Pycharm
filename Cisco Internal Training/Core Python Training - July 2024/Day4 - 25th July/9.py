class Student:
    def setdetails(self,name, std,loc):
        self.name=name
        self.std=std
        self.city=loc
        self.marks=list(map(int,self.loc.replace("-",",").split(",")))
        self.total=sum(self.marks)
    def show(self):
        print("name = ",self.name)
        print("std = ",self.std)
        print("city = ",self.city)
        print("marks = ", self.marks)
        print("total = ", self.total)
    def findtotal(self):
        print("total = ", self.total)
st1 = Student()
st1.setdetails("ravi","8th","blr")
st1.show()

# name = ravi
# std = 8th
# city = blr

#OR

st1 = Student()
st1.setdetails("ravi","8th","10-20-30-40-50")
st1.findtotal()
st1.show()

# name = ravi
# std = 8th
# marks = [10,20,30,40,50]
# total = 150
