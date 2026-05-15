#pytest methods are started with test_

def test_add(a=6,b=2):
    assert a+b == 8
def test_sub(a=6,b=2):
    assert a-b == 4
def test_mul(a=6,b=2):
    assert a*b == 12
def normal_func_not_execute_div(a=6,b=2):
    assert a/b == 3





