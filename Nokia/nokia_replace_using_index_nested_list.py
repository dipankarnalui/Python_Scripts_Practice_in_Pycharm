l1=[[1,2],[4,5],[7,8],6,5]
#replace 5 with 10 in nested list
for i in range(len(l1)):
    if type(l1[i]) == list:
        if 5 in l1[i]:
            pos=l1[i].index(5)
            print(pos)
            l1[i][pos] = 10
            print(l1[i][pos])
print(l1)