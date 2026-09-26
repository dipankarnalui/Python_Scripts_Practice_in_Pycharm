'''
Magic/Dunder methods (__init__, __str__, __len__, etc.)
'''

class Student:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Student name is {self.name}"
s = Student("John")
print(s.name)
print(s)

###############################################

class Team:
    def __init__(self, players):
        self.players = players
    def __len__(self):
        return len(self.players)
team = Team(["John", "Bob", "Mike"])
print(len(team))

###############################################

class Number:
    def __init__(self, value):
        self.value = value
    def __add__(self, other):
        return Number(self.value + other.value)
    def __str__(self):
        return str(self.value)
a = Number(10)
b = Number(20)
c = a + b
print(c)

