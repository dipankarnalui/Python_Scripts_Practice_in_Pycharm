import sys

import pytest

@pytest.mark.skipif(sys.platform == "win32", reason="Skip this test case as this is Windows OS")
def test_in_linux_only():
    assert True


