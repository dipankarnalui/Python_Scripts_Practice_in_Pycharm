import sys


class Stack:
    def __init__(self, max):
        self.arr = []
        self.top = -1
        self.max = max

    def push(self, value):
        if self.top == self.max - 1:
            print("Stack OverFlow")
            raise Exception("stack overflow")
        else:
            self.arr.append(value)
            self.top = self.top + 1

    def gettop(self):
        return self.top

    def pop(self):
        if self.top == -1:
            print("Stack underflow")
            raise Exception("Stack Under flow")
        else:
            res = self.arr.pop()
            print(res, "popped")
            self.top = self.top - 1


expr = "(((10+20)))"
st1 = Stack(10)
try:
    for elem in expr:
        if elem == "(":
            st1.push(elem)
        elif elem == ")":
            st1.pop()
except:
    print("Im-balanced")
    sys.exit(0)
print("res = ", st1.gettop())
try:
    if st1.gettop() == -1:
        print("Balanced")
    else:
        print("Im-Balanced")
except:
    print("Im-balanced")