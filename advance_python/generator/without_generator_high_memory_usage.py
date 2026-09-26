#Generators are particularly useful when dealing with large amounts of data.

def large_numbers():
    for i in range(1000000000):
        yield i

for num in large_numbers():
    if num == 5:
        break
