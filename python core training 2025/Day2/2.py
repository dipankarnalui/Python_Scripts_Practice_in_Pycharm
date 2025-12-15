data = "arun-blr-math-10-sci-20-soc-30"
#marks = ["10","20","30"]
#Total marks = 60
list_result=data.split("-")
print(list_result)

marks=list_result[3::2]
print(marks)
marks[0]=int(marks[0])
marks[1]=int(marks[1])
marks[2]=int(marks[2])

total=sum(marks)
print(total)
