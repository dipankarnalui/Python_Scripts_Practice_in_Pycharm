class Problem1(Exception):
    pass
class Problem2(Exception):
    pass
class Problem25(Exception):
    pass
try:
    print("block of code being executed")
    #raise  Problem2()
except Problem1:
   print("Action-1")
except Problem2:
   print("Action-2")
except:           # Generic catch block
   print("Action-3")
else:             # when there is "NO EXCEPTION"
   print("Action-4")
finally:          # always
   print("Action-5")