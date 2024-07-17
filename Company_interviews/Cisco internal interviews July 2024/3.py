d1={
    "raj":"1",
    "gokul":"2",
    "dip1":"3",
    "dip2":"4",
    "dip3":"5",
    "dip4":"6"
}

'''
#print odd IDs
d2={}
for k,v in d1.items():
    if int(v)%2 != 0:
        print(k)
        d2[k]=v
print(d2)
'''
#dict comprehension
#d2 = { k,v for k,v in d1.items(): if int(v)%2 != 0 }