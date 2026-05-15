import pytest


def test_list():
    assert [2,3]==[2,3]

def test_tuple():
    t1=(1,5,3,8)
    assert t1[0]==1

def test_dict():
    d1={"name":"dipankar",
        "age":33}
    assert d1["name"]=="dipankar"

def test_set():
    s1={1,8,3,8,1}
    assert len(s1)==3

def test_string():
    str="hello world"
    assert str.startswith("hello")

def test_float():
    a=1.2
    b=2.3
    assert pytest.approx(a+b) == 3.5



