'''
An abstract class in Python is a class that contains one or more abstract methods
and is intended to be inherited by subclasses.
It is created using ABC and @abstractmethod from the abc module.
'''

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        print("hello")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

dog = Dog()
dog.sound()

cat = Cat()
cat.sound()


animal = Animal() #error

