import os

fd = os.open("emp.txt", os.O_RDONLY)
data = os.read(fd, 1024)   # read 1024 bytes
print(data.decode())
os.close(fd)
