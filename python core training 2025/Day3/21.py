def add2nos(num1=0,num2=0):
    res = num1 + num2
    print("local variables = ",locals())
    return res


ans = add2nos()
print(ans)
ans = add2nos(5)
print(ans)
ans = add2nos(10,20)
print(ans)
