class Person:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age  # Private attribute

    # Getter method
    def get_age(self):
        return self.__age


p = Person("Alice", 30)
print(p.get_age())  # Output: 30
