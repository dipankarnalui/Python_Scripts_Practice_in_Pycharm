def mask(numlst, odd_even):
    print("mask")
    if odd_even=="odd":
        for i in range(len(numlst)):
            if numlst[i]%2==1:
                numlst[i]="*"
    elif odd_even=="even":
        for i in range(len(numlst)):
            if numlst[i]%2!=1:
                numlst[i]="*"
    else:
        print("invalid")

def partition_by2(numlst):
    print("partition_by2")
    res1=[]
    res2=[]
    mid=int(len(numlst)/2)
    print(mid)
    res1=numlst[:mid+1]
    res2=numlst[mid+1:]
    return res1 , res2


'''

solution:-
==========
arrlib.py
==========
def mask(alst,flag):
    if flag=="even":
       for i in range(len(alst)):
           if alst[i]%2==0:
              alst[i] = "*"
    elif flag=="odd":
       for i in range(len(alst)):
           if alst[i]%2!=0:
              alst[i] = "*"

def partition_by_2(alst):
    mid = len(alst)//2
    part1 = alst[:mid]
    part2 = alst[mid:]
    return part1, part2

'''
