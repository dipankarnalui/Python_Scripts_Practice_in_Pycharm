alst = [
        "ravi-blr",
        "hari-chn",
        "manu-mum",
        "guru-del"
       ]

for record in alst:
    flst = record.split("-")
    print(flst[0], flst[1][0].upper())

'''
record           flst             flst[0]        flst[1][0]
                  [0]    [1]
"ravi-blr"      ["ravi","blr"]    ravi           b
"hari-chn"      ["hari","chn"]    hari           c
"manu-mum"      ["manu","mum"]    manu           m
"guru-del"      ["guru","del"]    guru           d
'''
