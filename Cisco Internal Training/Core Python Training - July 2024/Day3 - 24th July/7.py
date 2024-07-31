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
ptab={}
for e in plst:
    #k,v=e.split("-")[0].upper(),e.split("-")[1]
    k,v=e.split("-")
    ptab[k.upper()]=v
print(ptab)