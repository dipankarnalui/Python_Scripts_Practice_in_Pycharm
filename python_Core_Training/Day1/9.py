#example of callback functions

#sort by city
plst = [
        "hdd-blr-50",
        "mon-chn-45",
        "cpu-mum-80",
        "prn-hyd-65",
        "usb-blr-75",
        "keb-chn-86"
       ]
# lambda returns the last field of the data
# x = "hdd-blr-50"
fn = lambda x : x.split("-")[1]
# sort them by last field - specify the lambda as a KEY
plst.sort(key = fn)
# display every elem line by line
print("\n".join(plst))