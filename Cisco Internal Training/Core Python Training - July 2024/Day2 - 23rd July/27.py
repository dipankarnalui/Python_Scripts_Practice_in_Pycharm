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
name=[]
marks=[]
for e in studlst:
    name.append(e.split("-")[0])
    marks.append(e.split("-")[1])
print(name)
print(marks)
l1=[]
for e in marks:
   l1.append(sum(list(map(int,e.split(",")))))
for name,total in zip(name,l1):
    print(f"{name} total is {total}")