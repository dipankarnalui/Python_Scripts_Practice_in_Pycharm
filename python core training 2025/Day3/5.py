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
s_name=input("Enter student name : ")
if s_name in studs.keys():
    loc,clas,*marks,grp=studs[s_name].replace("-",",").split(",")
    print("loc = ", loc)
    print("class = ", clas)
    print("marks = ",list(map(int,marks)))
    print("toal = ", sum(list(map(int,marks))))
    print("grp = ", grp)
    if grp in color.keys():
        print("grp color = ", color[grp]) 
