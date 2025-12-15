
city = {
        "blr" : 10,
        "chn" : 20,
        "mum" : 30,
        "del" : 40
       }

loc = "blr"
print("Value of blr = ",city[loc])      # 10
print("Value of blr = ",city.get(loc))  # 10

check = "hyd"
print("check whether hyd exists ", check in city) # False
print("Check whether chn exists ", "chn" in city) # True
print("Check whether 10  exists ", 10 in city)    # False

newvalue = 55
print("old value of mum = ",city["mum"]) # 30
city["mum"] = newvalue
print("New value of mum = ",city["mum"]) # 55
 
newcity = "pune"
newvalue = 26
print("BEFORE dict = ",city)
city[newcity] = newvalue
print("AFTER dict = ",city)
