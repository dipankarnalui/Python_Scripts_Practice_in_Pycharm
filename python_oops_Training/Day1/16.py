class Player:
  def __init__(self,name,team):
     self.name = name      # common data members
     self.team = team
  def show(self):
     print("Player details")
     print(f"Name = {self.name} Team = {self.team}")

# how we derive a class from BASECLASS
class Batsman(Player):
  def __init__(self,name,team,srate,cent):           #change1 #constructor cascading
      Player.__init__(self,name,team)                #change2 #constructor cascading
      self.srate = srate   # Special data members
      self.cent  = cent
  def display(self):
     print("Batsman Details")
     print(f"Srate = {self.srate} Cent = {self.cent}")

virat = Batsman("Virat Kohli","India", 150,75)

# Display the object like a dictionary
print(vars(virat))     # print(virat.__dict__)

#half-baked - not fully baked