import pytest

@pytest.mark.skip(reason="i want to skip this test")
def test_skip():
    pass

def test_not_skip():
    assert 2+3==5

def test_should_fail():
    assert 2+3==10

