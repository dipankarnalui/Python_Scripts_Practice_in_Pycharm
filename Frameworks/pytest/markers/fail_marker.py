import pytest

@pytest.mark.xfail(reason="expected failure as bug is not yet fixed")
def test_expected_fail():
    assert 1==2
