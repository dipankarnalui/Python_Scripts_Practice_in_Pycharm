#input_array = [1, 6, 9, 3, 2, 14, 10]
#output_array = [1, 3, 9, 2, 6, 10, 14]
#sort the odd numbers and even numbers.
#Output array will contain sorted odd numbers at first then even numbers


def sort_array(array):
    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                tmp = array[i]
                array[i] = array[j]
                array[j] = tmp


if __name__ == '__main__' :
    input_array = [1, 6, 9, 3, 2, 14, 10]
    output_array = [1, 3, 9, 2, 6, 10, 14]
    even = []
    odd = []

    for i in range(0, len(input_array)):
        print("Element = {} at Position {}".format(input_array[i],i))
        if input_array[i] % 2 != 1:
            print("Even")
            even.append(input_array[i])
        else:
            print("Odd")
            odd.append(input_array[i])

    print("Before sort Even Array = ", even)
    print("Before sort Odd Array = ", odd)
    sort_array(even)
    sort_array(odd)
    final = odd + even
    print("Sorted Array = ", final)

