#List all those elements thts is starting with "message"
'''
id  = "message13"
id = "messagety6"
id = "123message12"

re (^message)
/html/

'''

list=["message13","messagety6","123message12"]
for element in list:
    if element.startswith("mess"):
        print(element)


