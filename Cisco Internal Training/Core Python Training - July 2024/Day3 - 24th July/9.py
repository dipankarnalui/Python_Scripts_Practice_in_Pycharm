#Trick-1:-
#---------
plst = [
"dvd-10",
"mon-20",
"prn-30",
"cpu-40",
"hdd-50",
]

res = dict(e.split("-") for e in plst)
print(res)

'''
#Trick2:-
#---------
alst = ["ravi","kunal","pavan","mani"]
blst = [10,20,30,40]

res = dict(zip(alst,blst))
print(res)
'''