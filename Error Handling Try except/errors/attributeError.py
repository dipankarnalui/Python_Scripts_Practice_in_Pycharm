try:
    my_list = [1, 2, 3]
    my_list.add(4)  # Attempting to use an invalid method
except AttributeError:
    print("Error: 'list' object has no attribute 'add'.")
