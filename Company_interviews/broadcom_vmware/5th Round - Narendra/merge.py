import csv

file1="1.csv"
l1=[]
with open(file1, "r") as f1:
    csv1=csv.reader(f1)
    for csv1_line in csv1:
        print(csv1_line)
