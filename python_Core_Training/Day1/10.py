#sort based on total marks

studlist = [
            "arun-10,20,30",
            "yash-40,60,50",
            "guru-43,65,34",
            "manu-54,34,65"
           ]

fn = lambda x : sum(list(map(int,x.split("-")[1].split(","))))
studlist.sort(key = fn)
print(studlist)