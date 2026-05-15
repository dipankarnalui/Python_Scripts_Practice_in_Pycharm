from calculator import Calculator


class Test_Calculator():
    c = Calculator() #class variable #static variable #shared between all the objects
    def test_add(self):
        assert self.c.add(5,3) == 8
    def test_subtract(self):
        assert self.c.subtract(5,3) == 2
    def test_multiply(self):
        assert self.c.multiply(5,3) == 15
    def test_divide(self):
        assert self.c.divide(15,3) == 5
