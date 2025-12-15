data = "arun-blr-math,10,sci,20,soc,30"

#marks = ["10","20","30"]
#Total marks = 60

r=data.split(",")
print(r)

marks=r[1::2]
print(marks)

marks_int=list(map(int,marks))
print("total=",sum(marks_int))

marks_alternative=[int(e) for e in marks]
print("total=",sum(marks_alternative))


