try:
    my_dict = {'a': 1}
    print(my_dict['b'])  # Attempting to access a non-existing key
except KeyError:
    print("Error: Key not found in the dictionary.")
