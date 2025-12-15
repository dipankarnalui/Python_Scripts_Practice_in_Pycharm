      #   0   1    2  3   4   5  6   7
data = "arun-blr-math-10-sci-20-soc-30"

marks = data.split("-")[3::2]

print(marks)  # ["10", "20", "30"]

marks[0] = int(marks[0])
marks[1] = int(marks[1])
marks[2] = int(marks[2])

print(marks)  # [10,20,30]
print("Total marks = ",sum(marks))
