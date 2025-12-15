class Student:
    def __init__(self):
        self.name=None
        self.clas=None
        self.city=None 
    def setdetails(self,name,clas,city):
        self.name=name
        self.clas=clas 
        self.city=city 
    def show(self):
        print("name = ",self.name)
        print("clas = ",self.clas)
        print("city = ",self.city)   
st1 = Student()
st1.setdetails("ravi","8th","blr")
st1.show()
