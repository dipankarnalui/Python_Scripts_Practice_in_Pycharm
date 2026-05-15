import pytest

@pytest.fixture
def reusable_function():
    l1=[10,2,3,4,5,10]
    return l1

def test_reusable_function_test_case_1(reusable_function):
    l2=reusable_function
    assert l2.count(10) == 2

def test_reusable_function_test_case_2(reusable_function):
    l3=reusable_function
    assert len(l3)==6

def test_reusable_function_test_case_3(reusable_function):
    l4=reusable_function
    l4.append(90)
    assert l4[-1] == 90

def test_reusable_function_test_case_4(reusable_function):
    l5=reusable_function
    assert sum(l5) == 34
