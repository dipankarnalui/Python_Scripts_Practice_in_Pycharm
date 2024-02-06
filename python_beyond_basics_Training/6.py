numlst = [10,20,30,40,50]
for elem in numlst:
    elem = elem + 1
print("NUMLST",numlst)
for index in range(len(numlst)):
    numlst[index] = numlst[index] + 1
print("NUMLST",numlst)