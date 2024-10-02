with open("input.txt", "r") as f:
    full_data_str=f.read()
    print(type(full_data_str))
    print(full_data_str)

print("------------------------------------")
with open("input.txt", "r") as f:
    all_lines_list=f.readlines()
    print(type(all_lines_list))
    print(all_lines_list)
    for line in all_lines_list:
        print(line, end='')

print("------------------------------------")
with open("input.txt", "r") as f:
    one_line=f.readline()
    print(one_line)