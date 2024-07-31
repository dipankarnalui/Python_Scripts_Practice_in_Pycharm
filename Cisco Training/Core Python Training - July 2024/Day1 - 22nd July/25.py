data="arun-blr-math,10,sci,20,soc,30"
marks_list_str=data.split(",")[1::2]
print(marks_list_str)
#convert list of string to list of int using list comprehension
marks_list_int = [int(x) for x in marks_list_str]
print(marks_list_int)
print(sum(marks_list_int))