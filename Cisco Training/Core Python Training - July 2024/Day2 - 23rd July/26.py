alst = [
"blr-dvd-50",
"chn-mon-30",
"del-prn-25",
"blr-keb-60",
"mum-usb-65",
"del-hdd-20"
]

print(list(map(str,[e.split("-")[1] for e in alst])))
print(list(map(str,[e.split("-")[1] for e in alst if int(e.split("-")[2])>=50 ] )))
