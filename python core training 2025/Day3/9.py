plst = ["dvd-10",
        "mon-20",
        "prn-30",
        "cpu-40",
        "hdd-50",
       ]

res = dict(e.split("-") for e in plst )
print(res)

#OR

res={e.split("-")[0].upper():int(e.split("-")[1]) for e in plst}
print(res)

#OR

ptab={}
for elem in plst:
   key,value = elem.split("-")
   ptab[key.upper()] = int(value)
print(ptab)

