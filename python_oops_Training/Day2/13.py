class Person:
    def __init__(self):
        self.name = "vijay"
        self.city = "blr"
p1 = Person()
print(vars(p1))  # {"name":"vijay", "city":"blr" }

# it will be added
# since python classes are RUN TIME CLASSES
# we can add/delete data members on the fly
p1.company = "cisco"  # very important
print(vars(p1))

# del p1.company
# print(vars(p1))

Person.show = lambda x: print("Name", x.name, "City", x.city)
p1.show()