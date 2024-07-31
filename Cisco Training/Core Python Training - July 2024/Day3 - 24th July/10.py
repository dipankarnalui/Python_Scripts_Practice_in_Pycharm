#convert list into dict
'''
ptab = {
"DVD" : 10,
"MON" : 20,
"PRN" : 30,
"CPU" : 40,
"HDD" : 50
}
'''
plst = [
"dvd-10",
"mon-20",
"prn-30",
"cpu-40",
"hdd-50",
]
ptab=dict(e.split("-") for e in plst)
print(ptab)