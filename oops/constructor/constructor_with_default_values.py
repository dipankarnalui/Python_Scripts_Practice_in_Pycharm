class A():
    def __init__(self,age=10,name="Dipankar"):
        self.age=age
        self.name=name
    def show_data(self):
        print(self.age)
        print(self.name)
o=A()
o.show_data()

o=A(30,"XYZ")
o.show_data()
