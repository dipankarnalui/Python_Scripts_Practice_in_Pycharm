class Calculator:
    def __init__(self):
        print("Constructor called")
    def show(self):
        print("inside show")

obj1=Calculator()
obj1.__init__()
obj1.show()