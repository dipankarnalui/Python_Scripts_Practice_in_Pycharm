class Student:
  #parameterized constructor -
  def __init__(self,name,grade,marks):
     self.name = name
     self.grade = grade
     self.marks = list(map(int,marks.split(",")))
     self.total = 0
  def find_total(self):
     self.total = sum(self.marks)
  def show(self):
     print("%s %s %s %s" %(self.name,self.grade,self.marks,self.total))

st1 = Student()   # error out - since ctor expects args

# style-1 to create objects
st1 = Student("ravi","8th","10,20,30,40")
st2 = Student("manu","10th","50,60,70,80")

# style-2 to created objects - random order of passing args
st3 = Student(name="hari", grade="5th", marks = "40,50,60,70")
#st3 = Student(grade="5th",name="hari", marks = "40,50,60,70")
#st3 = Student(marks = "40,50,60,70",name="hari", grade="5th" )


st1.find_total()
st2.find_total()
st3.find_total()

st1.show()
st2.show()
st3.show()