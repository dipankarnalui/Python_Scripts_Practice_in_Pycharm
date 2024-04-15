prime_list = [1,3,5,7,11,3,13,5]
dup_removed_list=[]
for e in prime_list:
    if e not in dup_removed_list:
        dup_removed_list.append(e)
print(dup_removed_list)
'''
for e in dup_list:
    if e in prime_list:
        index=prime_list.index(e)
        print("ele = {}, index = {}".format(e,index))
print("prime_list = ", prime_list)
'''