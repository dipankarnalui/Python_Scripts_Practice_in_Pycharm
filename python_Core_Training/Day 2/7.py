import collections
import os
filename = input("Enter the filename : ")
if os.path.isfile(filename):
    f1 = open(filename,"r")
    words = f1.read().split()
    freq = collections.Counter(words)
    print("Most repeated word = ",freq.most_common(1))
    f1.close()
else:
    print("File Not Found")