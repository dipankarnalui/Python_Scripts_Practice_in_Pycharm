def numbers():
    yield 1
    yield 2
    yield 3
r=numbers() #this is a generator object
print(r)
print(next(r))
print(next(r))
print(next(r))