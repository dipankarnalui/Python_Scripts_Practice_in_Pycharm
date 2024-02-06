import arrlib
numlst = [1,2,3,4,5,6,7,8,9]
arrlib.mask(numlst, "odd")
print(numlst)  # [*,2,*,4,*,6,*,8,*]
arrlib.mask(numlst, "even")
print(numlst) # [1,*,3,*,5,*,7,*,9]
res1 , res2 = arrlib.partition_by2(numlst)
print(res1)  # [1,2,3,4]
print(res2)  # [5,6,7,8,9]
