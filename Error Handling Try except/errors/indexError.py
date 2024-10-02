try:
    my_list = [1, 2, 3]
    print(my_list[5])  # Attempting to access an index that doesn't exist
except IndexError:
    print("Error: Index out of range.")
