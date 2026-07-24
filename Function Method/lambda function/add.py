#Normal function
def add(a,b):
    return a+b

r=add(2,3)
print(r)

#convert the above normal function to lambda function
#function_name = lambda input_parameters : return_expression

add = lambda a,b: a+b
r=add(2,3)
print(r)

