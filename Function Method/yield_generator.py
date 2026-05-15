'''
def normal_function():
    return [1,2,3,4]
print(normal_function())
'''

def generate_numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

gen = generate_numbers()
print(type(gen))

print(next(gen))
print(next(gen))
print(next(gen))




