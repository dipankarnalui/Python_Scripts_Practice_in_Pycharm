def if_else(a,b):
    if a > b :
        return a
    else:
        return b
r=if_else(5,6)
print(r)


#convert to lambda

if_else=lambda a,b : a if a > b else b
print(if_else(5,6))


