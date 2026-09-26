class Duck():
    def sound(self):
        print("quak quak")

class Dog():
    def sound(self):
        print("bark")

def make_sound(animal):
    animal.sound()

dk=Duck()
make_sound(dk)

dg=Dog()
make_sound(dg)

