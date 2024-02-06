def mask(numlst,check):
    oddlst = numlst.copy()
    evenlst = numlst.copy()
    if str(check) == "odd":
        for i in range(0,len(oddlst)):
            if oddlst[i] % 2 == 1:
                #print("odd = ", oddlst[i])
                oddlst[i] = "*"
        return oddlst
    if str(check) == "even":
        for i in range(0,len(evenlst)):
            if evenlst[i] % 2 != 1:
                #print("even = ", evenlst[i])
                evenlst[i] = "*"
        return evenlst

def partition_by2(numlst):
    part_lst=numlst.copy()
    res1=numlst
    res2=numlst
    return res1, res2

numlst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
oddlst=mask(numlst, "odd")
print(oddlst)  # [*,2,*,4,*,6,*,8,*]

evenlst=mask(numlst, "even")
print(evenlst) # [1,*,3,*,5,*,7,*,9]

res1, res2 = partition_by2(numlst)
print(res1)  # [1,2,3,4]
print(res2)  # [5,6,7,8,9]
