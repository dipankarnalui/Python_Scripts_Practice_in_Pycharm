'''
def func1():
    print("fn1 called")

print(id(func1()))


a=12
b=3
print(id(a))
print(id(b))
a,b=b,a
print(id(a))
print(id(b))

#call by ref
'''

import os

n=4
#4 file
#n-1 file
#recursive
#dir1/dir2 with (n-1)files/dir3 with (n-1)files /dir4 with (n-1)files
path1="dir1"
path2="dir1/dir2"
path3="dir1/dir2/dir3"
def create_dir(n):
    for i in range(1,n):
        if n==1:
            os.makedirs(path1)
        if n==2:
            os.makedirs(path2)
            os.write(path2+"/1.txt")
        if n == 3:
            os.makedirs(path3)
            os.write(path2+"/1.txt")
            os.write(path2+"/2.txt")
if "__name__" == "__main__":
    if n > 1:
        create_dir(n)