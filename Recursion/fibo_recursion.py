'''
Why Recursive Fibonacci is Slow?
Because:
Same values are recalculated again and again
'''


#0,1,1,2,3,5,8,13,21,34,

def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

n=10
for i in range(n):
    print(fibo(i),end=',')
