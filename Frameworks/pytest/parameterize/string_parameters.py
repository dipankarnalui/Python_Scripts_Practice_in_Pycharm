import pytest

@pytest.mark.parametrize("single_parameter",[("hello"),("hi"),("hospital")])
def test_string_parameters(single_parameter):
    assert single_parameter.startswith("h")

    