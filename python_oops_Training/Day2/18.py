#decorator -- wrapper -- closer
def outer(fnref):
    def wrapper(*args,**kwargs):
        print(fnref.__name__,end=" ")  # before calling fn
        res = fnref(*args,**kwargs)
        return res
    return wrapper

@outer             # add = outer(add)
def add(a,b):      # older add-fun address is replaced by
   return a+b      # newer add-fun address

@outer
def express(a,b,c):
   return a-b+c

@outer
def square(a):
   return a*a

print(add(10,20))
print(express(1,2,3))
print(square(5))