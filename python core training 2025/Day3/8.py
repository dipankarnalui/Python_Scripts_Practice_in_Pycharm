plst = [
        "dvd-blr-10",
        "mon-chn-20",
        "prn-mum-30",
        "cpu-blr-40",
        "hdd-del-50",
       ]

ptab={}
for e in plst:
    device,city,price=e.split("-")
    ptab[device]=int(price)

print(ptab) 