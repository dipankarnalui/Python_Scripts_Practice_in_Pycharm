l1=[1,2,3,4,5,6,7,8,9,10]


for i in range(len(l1)):
    if l1[i]%2 == 0:
        if l1[i] == 6:
            continue
        print("even = ",l1[i])



