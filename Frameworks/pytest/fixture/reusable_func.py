import pytest

@pytest.fixture
def reusable_function():
    d1={"name":"dipankar"}
    return d1

def test_test_case_1(reusable_function):
    d2=reusable_function
    assert d2["name"] == "dipankar"

def test_test_case_2(reusable_function):
    d2=reusable_function
    d2["age"] = 10
    print(reusable_function)
    assert d2 == reusable_function

