
# collect all the city names from the LIST
# and store the city names in a NEW LIST
alst = [
        "ravi-blr",
        "hari-chn",
        "manu-mum",
        "guru-del"
       ]

# define a empty list to collect the CITY NAMES
newlst = []

# traverse on the list
for record in alst:
    # split the data based on the delimiter
    name,city = record.split("-")
   
    # append the city name to the EMPTY LIST
    newlst.append(city)

# outside the for - print it
print(newlst)  #["blr","chn","mum","del"]
