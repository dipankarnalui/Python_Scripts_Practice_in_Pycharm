import pytest

def read_file():
    with open("file.txt") as f:
        return f.read()

def test_read_file():
    with pytest.raises(FileNotFoundError):
        read_file()


