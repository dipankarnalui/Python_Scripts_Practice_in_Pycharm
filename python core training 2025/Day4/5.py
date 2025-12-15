
import os

print("Process ID       = ",os.getpid())
print("Curr Working Dir = ",os.getcwd())
print("Curr OS name     = ",os.name)

# excute shell commands within python program
os.system("hostname")   



import sys

print("Python Version = ",sys.version)
print("Exe file       = ",sys.executable)
print("Py Impl        = ",sys.implementation)
print("LIB PATH       = ",sys.path)
print("CMD LINE ARGS  = ",sys.argv) #  - command line args

