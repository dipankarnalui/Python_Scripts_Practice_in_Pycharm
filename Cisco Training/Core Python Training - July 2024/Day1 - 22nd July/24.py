data="arun-blr-math,10,sci,20,soc,30"
marks_list_str=data.split(",")
print(marks_list_str)
total=0
for e in marks_list_str:
    if e.isdigit():
        total = total + int(e)
print("Total marks = ", total)