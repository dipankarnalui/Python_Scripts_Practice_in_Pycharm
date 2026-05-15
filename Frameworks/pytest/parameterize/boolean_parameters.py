import pytest


def is_even(num):
    return num % 2 == 0

@pytest.mark.parametrize("num,bool_param",[(2,True),(3,False)])
def test_true(num,bool_param):
    assert is_even(num) == bool_param
