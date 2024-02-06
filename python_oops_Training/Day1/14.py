class Base:
    def __init__(self):
        print("Base-class Ctor")

class Derived(Base):
    def __init__(self):
        # we need to explicitly call the base class ctor
        # to enable CTOR CASCADING
        Base.__init__(self)
        print("Derived-class Ctor")

ob = Derived()
