class Person:
   def __init__(self):
       print("person created")
   def __del__(self):
       print("person deleted")
   def show(self):
       print("Show called")
p1 = Person()
p1.show()