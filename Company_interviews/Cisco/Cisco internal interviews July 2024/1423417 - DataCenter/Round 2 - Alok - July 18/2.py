#code is given
#Do white box testing
#Find the issues in the code
#Suggest code improvement
#needed for Code review by seniors
#Data Type checking, division by zero, boundary value analysis etc.
def fibonacci(n):
    """Returns the nth Fibonacci number."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
def test_fibonacci():
    """Tests the fibonacci function."""
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    print("All tests passed.")

if __name__ == "__main__":
    test_fibonacci()
