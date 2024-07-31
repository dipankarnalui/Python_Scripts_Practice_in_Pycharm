class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def show(self):
        print(f"name = {self.name}")
        print(f"marks = {self.marks}")
    def findtotal(self):
        self.total = sum(self.marks)
        print(f"total = {self.total}")
st1 = Student(name="ravi", marks = [10,20,30,40])
st1.show()  # name = ravi
            # marks = [10,20,30,40]
st1.findtotal() # total = 100
