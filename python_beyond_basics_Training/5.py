'''
>> special class - enumerate(collection)
>> read-write on mutable collection
>> designed for MUTABLE COLLECTION i.e list
>> Suitable - Inplace operations
>> bit slow compared to index based iterator
>> alst=[11,21,31,41,51]
   list(enumerate(alst))
   [(0, 11), (1, 21), (2, 31), (3, 41), (4, 51)]
'''
alst=[10,20,30,40,50]
print(alst)
                   #[(0, 11), (1, 21), (2, 31), (3, 41), (4, 51)]
for index,value in enumerate(alst):
    alst[index] = value + 4
print(alst)