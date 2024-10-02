try:
    # Attempting to convert an invalid string to an integer
    number = int("abc")
except ValueError:
    print("Error: Cannot convert the string 'abc' to an integer.")
