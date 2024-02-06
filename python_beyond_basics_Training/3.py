class Duck:
   def quack(self):
       print("duck says quack quack")
   def walk(self):
       print("duck can walk")
class Person:
   def talk(self):
       print("Person can talk")
   def walk(self):
       print("Person can walk")
class Book:
   def read(self):
       print("Read the Book")
if __name__ == "__main__":
    alst = []
    alst.append(Duck())   # walk() does it work ? yes
    alst.append(Person()) # walk()                yes
    alst.append(Duck())   # walk()
    alst.append(Person()) # walk()
    alst.append(Book())
    #print(alst)
    for elem in alst:
        #print(elem)
        elem.walk() # elem is obj -- which can't access walk of Book()
        if type(elem) == Duck: # anything specific place it here
            elem.quack()
        elif type(elem) == Person: # anything specific place it here
            elem.talk()