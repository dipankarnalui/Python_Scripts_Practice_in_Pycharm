with open("test_file.txt", "r") as f:
    all_lines_list=f.readlines()
    line_list_without_newlines = [line.strip() for line in all_lines_list if line.strip() ]
    print(line_list_without_newlines)
