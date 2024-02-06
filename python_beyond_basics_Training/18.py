class Stack:
    def __init__(self,max):
       self.arr = []
       self.top = -1
       self.max = max
    def push(self,value):
       if self.top == self.max-1:
          print("Warning : Stack OverFlow....")
       else:
          self.arr.append(value)
          self.top = self.top+1
    def pop(self):
       if self.top==-1:
          print("Warning : Stack Underflow....")
       else:
          res = self.arr.pop()
          print(res,"popped")
          self.top = self.top - 1
st1 = Stack(4)
st1.pop()
st1.push(10)
st1.push(20)
st1.push(30)
st1.push(40)
st1.push(50)
st1.pop()
st1.pop()
st1.pop()
st1.pop()
st1.pop()
