
studlst = [
           "ravi-40,30,10,60",
           "manu-54,37,87,50",
           "guru-76,80,66,40",
           "hari-58,45,95,45"
          ]

'''
for e in studlst:
    name,*marks=e.replace("-",",").split(",")
    print(f'{name} total is {sum(list(map(int,marks)))}')
'''

nested_list=[e.replace("-",",").split(",") for e in studlst]
for i in range(len(nested_list)):
    name,marks=nested_list[i][0],nested_list[i][1:]
    marks=[int(e) for e in marks]
    print(name, sum(marks))

'''
ravi total is 140
manu total is 228
guru total is 262
hari total is 243

>> single split
>> tuple unpacking
>> list comp or  map
'''