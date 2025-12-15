def adder(num1,num2):
   return num1+num2

#OR

adder = lambda x,y : x+y

print(adder(5,30))  # ?
print(adder(2,4))   # 



def convert(name):
    return name.split()[0]

#OR

convert = lambda x : x.split()[0]

print(convert("hari prasad")) 
print(convert("john peter")) 


