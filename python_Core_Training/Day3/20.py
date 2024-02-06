# user defined exception-
# should be a derived class of "Exception" class
class SameNumError(Exception):
   pass
try:
   num1 = input("Enter a num : ")
   num2 = input("Enter a num : ")
   num1 = int(num1)
   num2 = int(num2)
   if num1==num2:
      raise SameNumError("Number cannot be same")
   res = num1/num2
except ValueError as e1:
   print("Action1")
except ZeroDivisionError as e2:
   print("Action2")
except EOFError as e3:
   print("Action3")
except SameNumError as e4:
   print("Action4")
except Exception as e5:
   print("Action5",e5)
else:
   print(res)
finally:
   print("Cleanup Activity")

