'''
Enter student name : ravi
loc = blr
class = 8th
marks = [10,20,30,40]
total = 100
grp = grp3
grp color = green
'''
color = {
"grp1" : "red",
"grp2" : "blue",
"grp3" : "green"
}
studs = {
"ravi" : "blr-8th-10,20,30,40-grp3",
"hari" : "hyd-10th-60,30,50,51-grp1",
"manu" : "del-10th-60,70,20,52-grp2",
"guru" : "mum-10th-60,50,60,55-grp1",
}
student_name=input("Enter student name : ").lower()
if student_name in studs.keys():
    loc,cls,*marks,grp=studs[student_name].replace("-",",").split(",")
    grp_clr=color[grp]
    marks_list_int = list(map(int,marks))
    print(f"loc = {loc}")
    print(f"class = {cls}")
    print(f"marks = {marks_list_int}")
    print(f"total = {sum(marks_list_int)}")
    print(f"grp = {grp}")
    print(f"grp color = {grp_clr}")
else:
    print("invalid name")