#Find the strings for ERROR marker from the logging files in a directory path
#remove duplicate errors
import glob
path = "./"
text_files = glob.glob(path + "*.txt", recursive = True)
print(text_files)
tmp=[]
for tf in text_files:
    with open(tf, "r") as f:
        lines=f.readlines()
        for line in lines:
            first=line.split(",")[0]
            second=line.split(",")[1]
            if first == "ERROR":
                #remove duplicate
                if second not in tmp:
                    tmp.append(second)
print(tmp)



