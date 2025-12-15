data = "arun-blr-math-10-sci-20-soc-30"
#marks = ["10","20","30"]
#Total marks = 60
list_result=data.split("-")
print(list_result)

marks=[]
for e in list_result:
    if not e.isalpha():
        print(e)
        marks.append(int(e))
print(marks)

total=sum(marks)
print(total)


    
