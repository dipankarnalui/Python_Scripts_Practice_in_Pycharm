      #   0   1    2  3   4   5  6   7
data = "arun-blr-math-10-sci-20-soc-30"

marks = data.split("-")[3::2]

print(marks)  # ["10", "20", "30"]


marks=[int(e) for e in marks]

print(marks)  # [10,20,30]

print("total = ",sum(marks))
