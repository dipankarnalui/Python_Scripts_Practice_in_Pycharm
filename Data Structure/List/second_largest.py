def find_largest(l1):
    largest=max(l1)
    return largest

def delete_largest(l2, largest):
    l2.remove(largest)
    return l2

if __name__ == "__main__":
    n=int(input("Enter the number of elements: "))
    list1=[]

    for i in range(0, n):
        element = int(input("Enter the element for the position {} = ".format(i)))
        #list1.append(element)
        list1.insert(i, element)
        print(list1)

    largest = find_largest(list1)
    print("Largest Element = ", largest)

    list2=delete_largest(list1, largest)
    print("After deleting the largest, list1 = ", list2)

    second_largest=find_largest(list2)
    print("Second Largest Element = ", second_largest)