alst = [
        "ravi-blr",
        "hari-chn",
        "manu-mum",
        "guru-del"
       ]
'''
Expected:-
-----------
ravi B
hari C
manu M
guru D
'''
for index in range(0,len(alst)):
    print(alst[index].split("-")[0], alst[index].split("-")[1][0].upper())
