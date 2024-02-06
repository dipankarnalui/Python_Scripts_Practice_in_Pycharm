class Person:
    '''
    def set_details(self, name, age):
        self.name1=name
        self.age1=age
    '''

    #constructor method
    def __init__(self, name, age):
        self.name1 = name
        self.age1 = age

    def display(self):
        print(self.name1)

    def greet(self):
        if self.age1 > 10:
            print("Hello")
        else:
            print("Hi")

'''
p1=Person()
p1.set_details("Dipankar", 30) #similar to init function
p1.greet()
p1.display()
'''

o2=Person("Dipankar",30) #init function will take these 2 parameters as input
o2.greet()
o2.display()