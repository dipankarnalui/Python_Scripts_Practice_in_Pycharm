class Test:
    def method1(self):
        self.x = 10

    def display(self, y):
        self.x=y
        print(self.x)


t = Test()
t.display(10)