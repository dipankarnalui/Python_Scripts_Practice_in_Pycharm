#clouser used in function decorators
def OSFactory(a):
    print("Outer called Desinged for ",a)
    b=20
    def inner():
        print("Inner called")
        c=30
        res = b + c
        print("RESULT = ",res)
    return inner
fnptr1 = OSFactory("win")
fnptr2 = OSFactory("mac")
fnptr3 = OSFactory("linux")
fnptr4 = OSFactory("Unix")
fnptr1()
fnptr2()
fnptr3()
fnptr4()
