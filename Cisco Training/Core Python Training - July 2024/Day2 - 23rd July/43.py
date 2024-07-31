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
fn1 = lambda x : x.split("-")[0] # returns product name
fn2 = lambda x : x.split("-")[1] # returns location
fn3 = lambda x : int(x.split("-")[2]) # returns qty

# sort them by last field - specify the lambda as a KEY
plst.sort(key = fn3)
print(plst)
# display every elem line by line
print("\n".join(plst))
