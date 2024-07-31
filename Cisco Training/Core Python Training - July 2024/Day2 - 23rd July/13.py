alst = [
"ravi-blr",
"hari-chn",
"manu-mum",
"guru-del"
]
name_list=[]
city_list=[]
for i in range(len(alst)):
    name_list.append(alst[i].split("-")[0])
    city_list.append(alst[i].split("-")[1][0].upper())
#print(list(zip(name_list, city_list)))
for name,city in zip(name_list, city_list):
    print(name, city)

#performacne is better if we use e instead of i index, only reading not writing
#writing time, we can use index