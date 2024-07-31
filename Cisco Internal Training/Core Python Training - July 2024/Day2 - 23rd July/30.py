studlst = [
"ravi-40,30,10,60",
"manu-54,37,87,50",
"guru-76,80,66,40",
"hari-58,45,95,45"
]

for i in range(len(studlst)):
    name,*marks=studlst[i].replace("-",",").split(",")
    total = sum(list(map(int, marks)))
    print(f"{name} total is {total}")