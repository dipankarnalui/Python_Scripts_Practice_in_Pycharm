import pytest

class Test_A():

    @pytest.fixture(scope="class",autouse=True)
    def myfixture(self):
        print("myfixture")
    def test_1(self):
        print("test_1")
    def test_2(self):
        print("test_2")
    def test_3(self):
        print("test_3")