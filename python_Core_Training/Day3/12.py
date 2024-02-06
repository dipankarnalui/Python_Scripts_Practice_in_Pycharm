class Mytime: #() is old
    def __init__(self, hours=0, mins=0, secs=0):
        self.hours = hours
        self.mins = mins
        self.secs = secs
    def __add__(self, other):
        # "self"  alias of "t1" object
        # "other" alias of "t2" object
        temp = Mytime() #temp is an object of Mytimes() class
        temp.hours = self.hours + other.hours
        temp.mins = self.mins + other.mins
        temp.secs = self.secs + other.secs
        return temp
    def show(self):
        print("%s:%s:%s" % (self.hours, self.mins, self.secs))
t1 = Mytime(hours=10, mins=20, secs=15)
t2 = Mytime(hours=1, mins=10, secs=10)
res = t1 + t2
t1.show()  # 10:20:15
t2.show()  # 01:10:10
res.show()  # 11:30:25
