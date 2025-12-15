
menu = {
         "dosa" : 60,
         "idly" : 20,
         "upma" : 30,
         "vada" : 20,
         "poori": 50
       }

# prompt the user to enter the selection
item = input("Enter u r selected item : ").lower()

# search for selection - is it there ? 
if item in menu:
   print("Item is Found in the menu")
   print("Selected item = ",item)
   print("Price         = ",menu[item])
else:
   print("Selected item Not Found in the menu")
   print("Valid items are = ",menu.keys())
 