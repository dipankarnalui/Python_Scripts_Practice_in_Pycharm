'''
Expected:-
-----------
Enter your zone : south

First value = 50
Last value = 80
total = ?

Enter your zone : northwest

Invalid zone
'''

zones = {
"north" : "10-20-30-40",
"south" : "50-60-70-80",
"west" : "25-35-45-55",
"east" : "36-46-56-76"
}
zone_list=zones.keys()
z=input("Enter your zone : ").lower()
if z in zone_list:
    f,l=int(zones[z].split("-")[0]),int(zones[z].split("-")[-1])
    print(f"First value = {f}")
    print(f"Last value = {l}")
    total=sum(list(map(int,zones[z].split("-"))))
    print(f"Total = {total}")
else:
    print("Invalid zone")