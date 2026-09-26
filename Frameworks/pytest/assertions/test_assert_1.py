class Test_A():
    def add(self,a,b):
        self.a=a
        self.b=b
        return self.a+self.b
    def test_method_1(self):
        assert self.add(2,3)==5

