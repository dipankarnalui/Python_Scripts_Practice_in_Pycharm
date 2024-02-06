input_array = [1, 23, 3, 10, 5, 6, 8, 11]
output_array = [1, 3, 5, 11, 23, 6, 8, 10]

even = []
odd = []

for i in range(0, len(input_array) - 1):
    if input_array[i] % 2 == 0:
        print("even")
        even.append(input_array[i])
    else:
        print("odd")
        odd.append(input_array[i])
# even.sort()
# odd.sort()

# even=[8,6,10]
# sorted---->
for i in range(0, len(even) - 1):
    for j in range(i + 1, len(even) - 1):
        if even[i] > even[j]:
            tmp = even[i]
            even[i] = even[j]
            even[j] = tmp

for i in range(0, len(odd) - 1):
    for j in range(i + 1, len(odd) - 1):
        if odd[i] > odd[j]:
            tmp = odd[i]
            odd[i] = odd[j]
            odd[j] = tmp

output_array = odd.join(even)
print(output_array)

