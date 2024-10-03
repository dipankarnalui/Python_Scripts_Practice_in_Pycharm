class calculator:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.__c=c
    def get_values(self):
        print(self.__c)

a,b,c=1,2,3
cal=calculator(a,b,c)
cal.get_values()
print(cal.a)
print(cal.b)


#private variables cannot be accessible due to encapsulation
print(cal.c) #attribute error
print(cal.__c) #attribute error
