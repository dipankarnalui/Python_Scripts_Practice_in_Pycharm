alst = [
        "blr-dvd-50",
        "chn-mon-30",
        "del-prn-25",
        "blr-keb-60",
        "mum-usb-65",
        "del-hdd-20"
       ]
prodname=[]
above50=[]



for e in alst:
    city, product, price = e.split("-")
    prodname.append(product)
    if int(price) >= 50:
        above50.append(product)
print(prodname)
print(above50)

