class student:
    def setdetails(self,name,std,city):
        self.name = name
        self.std = std
        self.city = city
    def show(self):
        print("Name = ",self.name)
        print("STD = ", self.std)
        print("City =  ", self.city)
st1 = student()
st1.setdetails("ravi","8th","blr")
st1.show()