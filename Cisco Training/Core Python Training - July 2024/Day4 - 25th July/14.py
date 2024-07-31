class Student:
  def __init__ (self, name = "no name", marks = [0,0,0,0]):
    self.name = name
    self.marks = marks

  def show(self):
    print("Name =",self.name)
    print("Marks =",self.marks)

  def findtotal(self):
    print(sum(self.marks))


st1 = Student(name="ravi", marks = [10,20,30,40])

st1.show()  # name = ravi
            # marks = [10,20,30,40]

st1.findtotal() # total = 100
