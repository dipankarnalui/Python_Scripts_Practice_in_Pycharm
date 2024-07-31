class Vehicle: # BASE CLASS
    def start_engine(self):
        print("Engine Started")


class Car(Vehicle): # DERIVED CLASS
    def open_sunroof(self):
        print("Sunroof opened")

ob = Car()
ob.start_engine() # valid / invalid ?
ob.open_sunroof()
