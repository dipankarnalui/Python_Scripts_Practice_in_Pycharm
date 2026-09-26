def linear_search(a,target):
    for i in range(len(a)-1):
        if a[i]==target:
            print(f"target {target} found at location {i}")
            break

a=[12,90,23,45,25,87,1,20,72,10,67,28,101]
target=67
linear_search(a,target)