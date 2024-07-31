alst = [
"ravi-blr",
"hari-chn",
"manu-mum",
"guru-del"
]
name_list=[]
city_list=[]
for i in range(len(alst)):
    print(alst[i].split("-")[0],alst[i].split("-")[1][0].upper())



#performacne is better if we use e instead of i index, only reading not writing
#writing time, we can use index