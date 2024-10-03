my_dict = {'apple': 5, 'banana': 3, 'cherry': 8, 'date': 2}

# Sorting the dictionary by values (ascending order)
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

print(sorted_dict)
