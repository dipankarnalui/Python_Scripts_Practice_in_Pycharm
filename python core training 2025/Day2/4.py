marks=["10","20", "30"]

#list comprehension
#Output = [ <Operation> for e in <input> ]
result= [ int(e) for e in marks ]
print(result)

#functional programming
#map
# <Output> = list(map(<operation>,<inut>))

result_of_map = list(map(int,marks))
print(result_of_map)
