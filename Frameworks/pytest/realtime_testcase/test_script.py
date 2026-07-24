import CalculatorCode

class Test_Calculator():
    c= CalculatorCode.Calculator()
    def test_add(self):
        assert self.c.add(1,2) == 3
    def test_subtract(self):
        assert self.c.subtract(1,2) == -1





