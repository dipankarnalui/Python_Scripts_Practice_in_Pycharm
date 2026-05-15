import calculator

def test_replace_function(monkeypatch):
    #fake function
    def mock_func():
        return 5
    #replace function using setattr
    monkeypatch.setattr(calculator, "get_value", mock_func)

    assert calculator.mul() == 100
