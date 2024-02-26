# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for i in range(1, n + 1):
    l1 = []
    count = i
    for e in range(count):
        l1.append('*')
        # print(l1)
    print(*l1) #star to print in single line

