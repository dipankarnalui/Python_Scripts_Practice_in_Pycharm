def find_second_largest(l1):
    #remove duplicate
    l2=list(set(l1))
    print("After removing duplicate = ",l2)
    l2.sort()
    print("After sorting = ", l2)
    return l2[-2]
if __name__ == "__main__":
    n=int(input("Enter the number of elements: "))
    l1=[]
    for i in range(0,n):
        element=int(input("Enter the element for l1[{}] = ".format(i)))
        l1.insert(i,element)
        print(l1)
    second_largest=find_second_largest(l1)
    print("Second largest element = ",second_largest)