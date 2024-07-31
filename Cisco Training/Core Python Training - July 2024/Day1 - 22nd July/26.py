data="north-sales-10-20-30-40-50-blr-chn"
list_of_str=data.split("-")
print(list_of_str)
list_of_int=[]
for x in list_of_str:
    if x.isdigit():
        list_of_int.append(x)
print(list_of_int)
list_of_int_2=list(map(int,list_of_int))
print("Total = ",sum(list_of_int_2))