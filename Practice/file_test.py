with open("my_log.log",'r') as f:
    all_lines=f.readlines()
    for line in all_lines:
        print(line, end = "")