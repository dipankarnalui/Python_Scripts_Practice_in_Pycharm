import pytest

@pytest.mark.parametrize("a,b,result",[(1,2,3),(10,20,30)])
def test_add(a,b,result):
    assert a + b == result