'''
Expected:-
----------
ravi total is 140
manu total is 228
guru total is 262
hari total is 243
>> single split
>> tuple unpacking
>> list comp or map
'''
studlst = [
"ravi-40,30,10,60",
"manu-54,37,87,50",
"guru-76,80,66,40",
"hari-58,45,95,45"
]

for i in range(len(studlst)):
    name=studlst[i].split("-")[0]
    marks=studlst[i].split("-")[1]
    total = sum(list(map(int, marks.split(","))))
    print(f"{name} total is {total}")