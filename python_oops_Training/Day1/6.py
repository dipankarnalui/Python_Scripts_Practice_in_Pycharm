class Student:
    def setvalues(self,name,std,marks):
        self.name=name
        self.std=std
        self.marks=marks
    def find_total(self):
        l1=self.marks.split(",")
        i1=list(map(int,l1)) #convert str to int in list
        self.total=sum(i1)
    def show(self):
        print("Name = ",self.name)
        print("Grade = ",self.std)
        print("Marks = ",self.marks)
        print("Total = ",self.total)
    def compare_total(self,other):
        if self.total > other.total:
            print("Self.Total = ",self.total)
            print("other.Total = ",other.total)
            print(self.name, "has scored better than", other.name)
        else:
            print("Self.Total = ", self.total)
            print("other.Total = ", other.total)
            print(other.name, "has scored better than", self.name)
st1 = Student()
st1.setvalues("ravi", "8th", "10,20,30,40")
st2 = Student()
st2.setvalues("manu", "10th", "40,50,60,70")
st1.find_total()
st2.find_total()
st1.show() # name = ravi
# grade = 8th
# marks = [10,20,30,40]
# total = 100
st1.compare_total(st2) # "manu has scored better than ravi"  ==> # #Student.compare_total(st1,st2)

