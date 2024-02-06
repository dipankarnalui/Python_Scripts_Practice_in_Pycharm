plst = ["dvd-10",
        "mon-20",
        "prn-30",
        "cpu-40",
        "hdd-50",
       ]
res = dict(e.split("-") for e in plst)
print(res)