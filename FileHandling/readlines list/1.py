with open("test_file.txt","r") as f2:
    all_lines_list=f2.readlines()
    for line in all_lines_list:
         if line.strip():
             #print(line, end="")
             print(line.strip())

