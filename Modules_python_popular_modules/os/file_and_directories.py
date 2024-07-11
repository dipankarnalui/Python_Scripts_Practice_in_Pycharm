import os
import pathlib

#cwd = current working dir
print(os.getcwd())

#ls cwd
print(os.listdir())

#mkdir
#os.mkdir("dir3")

#cd
os.chdir("dir1")

#touch
pathlib.Path("file1.txt").touch()

with open("file1.txt","w") as f:
    f.write('this is line 1 \n')
    f.write('this is line 2 \n')
    f.write('this is line 3 \n')
    f.close()

with open("file1.txt","r") as f1:
    lines=f1.read()
    print(lines.splitlines())
