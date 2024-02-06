def OSFactory(a):
    #print("Outer called")
    b=20
    def inner(arch):
        #print("Inner called")
        c=30
        res = b + c
        print("RESULT = ",res,a,arch)
    return inner
fnptr1 = OSFactory("win")
fnptr2 = OSFactory("mac")
fnptr1("win32")
fnptr1("win64")
fnptr2("x86")