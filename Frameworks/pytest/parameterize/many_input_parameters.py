import pytest

@pytest.mark.parametrize("a,b,expected",[(1,2,3), (4,5,9), (7,8,15)])
def test_add(a,b,expected):
    assert a+b==expected

    