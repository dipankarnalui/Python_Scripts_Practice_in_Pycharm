'''
Expected:-
----------
ravi total is 140
manu total is ?
guru total is ?
hari total is ?
Duration : 10 mins
Time     : 11.55 to 12.05
'''
studlst = [
           "ravi-40,30,10,60",
           "manu-54,37,87,50",
           "guru-76,80,66,40",
           "hari-58,45,95,45"
          ]

for ele in studlst:
    name, marklist = ele.split("-")
    #print(name,marklist)
    total = 0
    #mlist = list(map(int, marklist))
    mlist = list(map(int, marklist.split(",")))
    print(mlist)
    total = sum(mlist)
    print(name , " total is " ,total)
