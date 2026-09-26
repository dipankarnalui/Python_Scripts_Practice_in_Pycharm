import pytest


@pytest.fixture(scope="module", autouse=True)
def myfixture():
    print("myfixture")


class Test_A:
    def test_1(self):
        print("test_1")

    def test_2(self):
        print("test_2")

    def test_3(self):
        print("test_3")


class Test_B:
    def test_4(self):
        print("test_4")

    def test_5(self):
        print("test_5")

    def test_6(self):
        print("test_6")