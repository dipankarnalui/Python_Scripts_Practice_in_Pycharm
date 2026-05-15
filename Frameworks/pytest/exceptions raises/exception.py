import pytest

def divide(a,b):
    return a/b
def test_divide():
    with pytest.raises(ZeroDivisionError):
        divide(10,0)


def validate_age(age):
    if age < 0:
        raise ValueError("Age can not be negative")
def test_validate_age():
    with pytest.raises(ValueError):
        validate_age(-10)

