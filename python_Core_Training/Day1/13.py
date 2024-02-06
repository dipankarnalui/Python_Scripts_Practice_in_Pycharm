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
name=input("Enter student name : ")
if name in studs:
    record=studs[name]
    new=record.replace("-"," ")
    loc,clas,marks,grp=new.split(" ")
    print("loc = ",loc)
    print("class = ",clas)
    marks=list(map(int,marks.split(",")))
    print("marks = ", marks)
    total = sum(marks)
    print("Total = ", total)
    print("grp = ", grp)
    print("grp color= ", color[grp])

else:
    print("student not found in dict")


'''
Expected:-
----------
 Enter student name : ravi
 loc   = blr
 class = 8th
 marks = [10,20,30,40]
 total = 100
 grp   = grp3
 grp color = green
'''