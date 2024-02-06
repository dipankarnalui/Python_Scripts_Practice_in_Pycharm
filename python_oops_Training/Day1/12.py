class Sample:
    def __init__(self):
        self.__data = 10
        self._city  = 20
        self.temp   = 30

ob1 = Sample()
#print("DATA = ",ob1.__data) #private
print("CITY = ",ob1._city)   #semi private
print("TEMP = ",ob1.temp)    #public
