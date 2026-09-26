def bubble_sort(a):
    for i in range(len(a)-1):
        for j in range(i+1,len(a)-1):
            if a[j] > a[i]:
                a[i],a[j]=a[j],a[i]
    print(a)
a=[23,45,67,49,200,374,6263,91,3,56,1]
bubble_sort(a)

