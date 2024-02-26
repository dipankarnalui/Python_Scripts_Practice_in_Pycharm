class FileRead:
    def __init__(self,fname):
        print("contructor called")
        self.fname=fname
    def store_into_dic(self):
        # read file and print the file content
        d1 = {}
        with open(self.fname, "r") as f:
            # all_lines=f.readlines()
            all_lines = f.read().splitlines()  # to remove /n
            for line in all_lines:
                if line.startswith("IP"):
                    k = line.split("=")[0]
                    v = line.split("=")[1]
                    d1[k] = v
        return d1
fname="simple.txt"
obj=FileRead(fname)
result=obj.store_into_dic()
print(result) #print dic

for key,val in result.items():
    print(key + " : " + val)