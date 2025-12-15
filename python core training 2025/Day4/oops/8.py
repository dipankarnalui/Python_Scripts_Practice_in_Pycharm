class Student:
    def __init__(self,name,std):
        self.name=None 
        self.std=None 
        self.marks=None
    def setdetails(self,name,std,marks):
        self.name=name
        self.std=std
        self.marks=marks 
    def findtotal(self):
        self.marks=list(map(int,self.marks.split("-")))
        self.total=sum(self.marks)
    def show(self):
        print("name = ", self.name)
        print("std = ", self.std)
        print("marks = ", self.marks)
        print("total = ", self.total)
st1 = Student()
st1.setdetails("ravi","8th","10-20-30-40-50")
st1.findtotal()
st1.show()
