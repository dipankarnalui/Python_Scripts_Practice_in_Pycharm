#pure shallow copy example

import copy

l1 = [[1, 2], [3, 4]]
l2 = copy.copy(l1)

l1[0].append(99)

print(l1)  # [[1, 2, 99], [3, 4]]
print(l2)  # [[1, 2, 99], [3, 4]]

