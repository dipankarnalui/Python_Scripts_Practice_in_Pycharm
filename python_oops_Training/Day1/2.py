class Circle:

    def setradius(self, r):
        self.radius = r  # given value
        self.area = 0  # we need to find it later

    def findarea(self):
        self.area = 3.14 * self.radius ** 2

    def showarea(self):
        print("Area = ", self.area)


# main program
ob1 = Circle()  # create an object
ob1.setradius(2.5)  # set the values
ob1.showarea()  # verify
ob1.findarea()  # operations
ob1.showarea()  # verify
'''
Note:
>> there is no
static
allocation in python
>> every
object is HEAP - BASED
object

'''

