def morning(name):
    print("Good morning",name)
    return "success"

def evening():
    print("Happy evening")


print("main program")
names=["bhupesh","dipankar","jagdish","monika"]

for item in names:
    result = morning(item)
    print(result)


