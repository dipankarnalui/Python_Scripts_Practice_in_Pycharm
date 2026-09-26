import pytest

class Test_Class():
    @pytest.fixture(scope='function',autouse=True)
    def my_fixture(self):
        print("myfixture is called")

    def test_method1(self):
        print("test_method1")
    def test_method2(self):
        print("test_method2")
    def test_method3(self):
        print("test_method3")
