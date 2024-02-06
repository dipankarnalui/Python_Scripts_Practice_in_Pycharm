class Base:
    def __init__(self):
        print("Base-class Ctor")

class Derived(Base):
    def __init__(self):
        print("Derived-class Ctor")

ob = Derived()
