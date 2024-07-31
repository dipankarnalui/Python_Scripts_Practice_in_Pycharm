'''
ravi B
hari C
manu M
guru D
print(alst) # still the data should be intact
Note: use the appor iterator - forward/reverse/index/parallel
'''

alst = [
"ravi-blr",
"hari-chn",
"manu-mum",
"guru-del"
]
name_list=[]
city_list=[]
for e in alst:  #forward iterator #read purpose #faster
    name_list.append(e.split("-")[0])
    city_list.append(e.split("-")[1][0].upper())
print(list(zip(name_list, city_list)))


#performacne is better if we use e instead of i index, only reading not writing
#writing time, we can use index