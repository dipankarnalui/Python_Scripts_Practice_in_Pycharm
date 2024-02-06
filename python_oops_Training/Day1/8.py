class Sample:
    def __init__(self): # constructor
        print("object created")
    def __del__(self): # destructor
        print("object destroyed")
    def show(self): # normal method
        print("Hello Sample")


ob = Sample() # object got created
ob.show() # Calling method

# end of main program - Dtor is called
