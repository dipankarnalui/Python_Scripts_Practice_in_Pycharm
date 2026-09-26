with open("mytest_file.txt","w") as f:
    f.writelines("hello")
f.close()

with open("test.txt","r") as f:
    all_lines=f.readlines()
    for line in all_lines:
        print(line.strip())