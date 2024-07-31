class Problem1(Exception): # user defined exception
    pass
class Problem2(Exception): # user defined exception
    pass
class Problem25(Exception): # user defined exception
    pass
try:
    print("block of code being executed")
    #raise Problem1()
    #raise Problem2()
    #raise Problem25()
except Problem1:
    print("Action-1")
except Problem2:
    print("Action-2")
except: # Generic catch block
    print("Action-3")
else: # when there is "NO EXCEPTION"
    print("Action-4")
finally: # always
    print("Action-5")
    print("CleanUp")