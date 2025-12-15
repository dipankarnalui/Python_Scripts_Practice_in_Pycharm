class CricketPlayer:
   def play(self):
       print("Played")
   def show_role(self):
       print("NOTHING is said")

class Bowler(CricketPlayer):
   def bowl(self):
       print("bowled")
   def show_role(self):
       print("I am a Bowler")

class Batsman(CricketPlayer):
   def bats(self):
       print("Batting")
   def show_role(self):
       print("I am a Batsman")


ob1 = Bowler() 
ob2 = Batsman()
ob1.bowl()    #  
ob2.bats()    #
ob1.show_role()   # works ?
ob2.show_role()   # works ?

#MRO  = Method Resolution Order

print("MRO of Bowler class = ",Bowler.__mro__)
print("MRO of Batsman class = ",Batsman.__mro__)
