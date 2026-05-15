import pytest

def add(a,b):
    return a+b

def test_add():
    pytest.raises(TypeError, add, 1,"2")
    