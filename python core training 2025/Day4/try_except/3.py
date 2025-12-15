
try:
   num1 = input("Enter a num : ")
   num2 = input("Enter a num : ")
   num1 = int(num1)
   num2 = int(num2)
   res = num1/num2
except ValueError as e1:
   print("Action1")
except ZeroDivisionError as e2:
   print("Action2")
except EOFError as e3:
   print("Action3")
except Exception as e4:  # un-listed exception
   print("Action4")
else:
   print("RESULT = ",res)

