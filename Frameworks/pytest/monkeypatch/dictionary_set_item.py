import pytest

d1={"name":"dip"}

def test_dict(monkeypatch):
    monkeypatch.setitem(d1, "name", "dipankar")
    assert d1["name"] == "dipankar"
