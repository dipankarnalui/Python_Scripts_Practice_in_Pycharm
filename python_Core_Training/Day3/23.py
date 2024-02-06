import time
print(time.localtime())   # returns current date & Time like a structure
print(time.localtime().tm_year)
print(time.localtime().tm_mon)
import datetime
print(datetime.date.today())
print(datetime.datetime.now())
print(datetime.datetime.now().strftime("%a %b %d %m %y"))