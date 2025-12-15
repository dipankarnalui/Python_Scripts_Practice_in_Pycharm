studlst = [
           "ravi-40,30,10,60",
           "manu-54,37,87,50",
           "guru-76,80,66,40",
           "hari-58,45,95,45"
          ]

for elem in studlst:
   name,*marks = elem.replace("-",",").split(",")
   marks = [int(e) for e in marks]
   print(name,sum(marks))

