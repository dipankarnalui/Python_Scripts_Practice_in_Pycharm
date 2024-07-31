alst = [
"blr-dvd-50",
"chn-mon-30",
"del-prn-25",
"blr-keb-60",
"mum-usb-65",
"del-hdd-20"
]
'''
prodname = [dvd,mon,prn,keb,usb,hdd]
above50 = [dvd,keb,usb]
'''
prodname=[]
above50=[]
for e in alst:
    prodname.append(e.split("-")[1])
    if int(e.split("-")[2]) >= 50:
        above50.append(e.split("-")[1])
print(prodname)
print(above50)