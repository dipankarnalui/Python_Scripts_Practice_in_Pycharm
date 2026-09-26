class A():
    name="Dipankar" #public
    _age=20 #protected
    __sal=10 #private

obj=A()
print(obj.name)
print(obj._age)
print(obj._A__sal)   #name mangling is only for private variable



