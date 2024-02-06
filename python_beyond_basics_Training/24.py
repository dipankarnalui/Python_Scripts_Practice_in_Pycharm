import itertools
alst = [1,2,3,4,5,6,7,8,9,10]
res = filter(lambda x : sum(x)==8, itertools.combinations(alst,2))
print(list(res))