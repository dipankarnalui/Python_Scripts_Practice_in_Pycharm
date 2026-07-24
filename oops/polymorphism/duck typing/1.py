class Duck:
    def speak(self):
        print("Quack!")

class Dog:
    def speak(self):
        print("Woof!")

def make_it_speak(animal):
    animal.speak()

duck = Duck()
dog = Dog()

make_it_speak(duck)  # Quack!
make_it_speak(dog)   # Woof!