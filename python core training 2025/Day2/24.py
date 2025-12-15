#Demo for filter the data :-
#---------------------------
# filter the emp's working in "blr"

alst = [
        "ravi-blr",
        "hari-chn",
        "manu-mum",
        "guru-BLR",
        "ramu-Blr",
        "giri-del",
        "manu-blr"
       ]

# traverse the list
for elem in alst:
    # split the element
    name,city = elem.split("-")

    # check the condition
    if city.lower() == "blr":
        print(name)

