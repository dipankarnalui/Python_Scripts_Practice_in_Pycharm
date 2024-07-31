def mask(numlst,odd_even):
    print(numlst)
    if odd_even == "odd":
        for i in range(len(numlst)):
            if numlst[i]%2!=0:
                numlst[i]="*"

    if odd_even == "even":
        for i in range(len(numlst)):
            if numlst[i]%2 == 0:
                numlst[i]="*"

def partition_by2(numlst):
    mid=len(numlst)//2
    part1=numlst[:mid]
    part2 = numlst[mid:]
    return part1,part2
