class A():
    v1=1   #public variable
    _v2=2  #protected variable
    __v3=3 #private variable

    def show_data(self):
        print("v1 = ",self.v1)
        print("_v2 = ", self._v2)
        print("__v3 = ",self.__v3)

obj=A()
print(obj.v1)

print(obj._v2)
#print(obj.__v3)  #private variable can not be accessed directly

print(obj._A__v3)  #another way to call private variable using name mangling

#better approach to use a public method to call the private variable
obj.show_data()

