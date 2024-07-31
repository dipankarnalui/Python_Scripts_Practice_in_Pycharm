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
    if city.lower() == "blr":
        print(city)
    # append the city name to the EMPTY LIST
    newlst.append(city)
# outside the for - print it
print(newlst) #["blr","chn","mum","del"]
