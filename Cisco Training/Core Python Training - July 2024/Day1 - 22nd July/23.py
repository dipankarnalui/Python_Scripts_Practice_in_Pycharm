data="arun-blr-math,10,sci,20,soc,30"
marks_list_str=data.split(",")[1::2]
#convert list of string to list of int using map
mark_list_int=list(map(int,marks_list_str))
print("Total Marks = ",sum(mark_list_int))