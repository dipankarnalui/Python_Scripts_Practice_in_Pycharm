zones = {
         "north" : "10-20-30-40",
         "south" : "50-60-70-80",
         "west"  : "25-35-45-55",
         "east"  : "36-46-56-76"
        }

zone=input("Enter your zone: ")
if zone in zones.keys():
    print(zone)
    values=zones[zone].split("-")
    print(values)
    first=int(values[0])
    last=int(values[-1])
    total=sum(list(map(int,values)))
    print(first, last, total)
else:
    print("Invalid zone")

