import glob
path = "C:\Users\dnalui\Python_Project\Python_Scripts_Practice\FileHandling\file_read"
text_files = glob.glob(path + "*.txt")
for text_file in text_files:
    with open(text_file,"r") as f:
        all_lines = f.readlines()
        for line in all_lines:
            print(line.strip())
