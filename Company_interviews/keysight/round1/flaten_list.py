input = [1, [2, [3, 4], 5], 6]
#o = [1,2,3,4,5,6]
l2=[]
def flaten_list(l):
    for e in l:
        if type(e) != list:
            l2.append(e)
        else:
            flaten_list(e)
flaten_list(input)
print(l2)

