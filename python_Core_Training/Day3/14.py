class Player:
   def __init__(self,name,team):
       print("Player ctor called")
       self.name = name
       self.team = team
   def show(self):
       print(self.name,self.team)
class Bowler(Player):   # we inherit a class
   def __init__(self, name, team, nwkts, ecorate):
       Player.__init__(self, name, team)  # ctor cascasding
       print("Bowler ctor called")
       self.nwkts = nwkts
       self.ecorate = ecorate
   def display(self):
       print(self.nwkts,self.ecorate)
hardik = Bowler("hardik","India",2,3.5)
# theory Bowler should have how many data members - 4
print(vars(hardik))