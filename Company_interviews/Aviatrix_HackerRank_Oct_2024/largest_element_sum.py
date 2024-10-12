# Find the sum of two largest elements of a list, the two elements should not be adjacent to each other

# Sample input = [1,3,2,6,9]
str1 = input("Enter elements as string, Example: [1,3,2,6,9]  = ")

str_l1 = []
for e in str1:
    if e == '[' or e == ']' or e == ',':
        pass
    else:
        str_l1.append(e)
l1 = list(map(int, str_l1))
l2 = []


def find_largest(l1):
    l2 = l1.copy()
    l2.sort()
    largest, second_largest, third_largest = l2[-1], l2[-2], l2[-3]
    return largest, second_largest, third_largest


def check_if_two_elements_are_adjacent(l1, e1, e2):
    index_of_e1 = l1.index(e1)
    index_of_e2 = l1.index(e2)
    # print(f"l1={l1},e1={e1},e2={e2}, index_of_e1={index_of_e1}, index_of_e2={index_of_e2}")
    if index_of_e1 + 1 == index_of_e2 or index_of_e2 + 1 == index_of_e1:
        return True
    else:
        return False


result = find_largest(l1)
largest, second_largest, third_largest = result[0], result[1], result[2]

if not check_if_two_elements_are_adjacent(l1, largest, second_largest):
    sum = largest + second_largest
elif not check_if_two_elements_are_adjacent(l1, largest, third_largest):
    sum = largest + third_largest
print(sum)


