'''
Expected:-
----------
prodname = [dvd,mon,prn,keb,usb,hdd]
above50  = [dvd,keb,usb]
Duration : 10 mins
Time     : 11.37 to 11.47
Trick    : replace "-" by spaces & then split by space
Trick    : regular expression split
'''
alst = [
        "blr-dvd-50",
        "chn-mon-30",
        "del-prn-25",
        "blr-keb-60",
        "mum-usb-65",
        "del-hdd-20"
       ]
prodname= []
above50 = []
for ele in alst:
    city,prod,price = ele.split("-")
    #print(city,prodname,price)
    prodname.append(prod)
    if int(price) >= 50:
        above50.append(prod)
print(prodname)
print(above50)

