def cal(*a,**b):
    print(type(a))
    print(type(b))
    return a,b

r=cal(1,2,3,age=1,name="dipankar")
print(r)
print(type(r))

