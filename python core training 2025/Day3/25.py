import os

def grep(filename="one.txt",word="sample"):
    if os.path.isfile(filename):
       with open(filename) as f1:
          for line in f1:
             if word in line:
                print(line)
    else:
       print("Error = File not Found")
grep()
