start_ip = "10.0.0.245"
count = 30 #num_of_host

#valid IP - Regex
#254 last IP
#last digit 254 -- count =10, throw error ""this many not possible

'''
print list of host
10.0.0.1
10.0.0.2
10.0.0.3
...
10.0.0.50
'''

first=int(start_ip.split(".")[0])
sec=int(start_ip.split(".")[1])
third=int(start_ip.split(".")[2])
fourth=int(start_ip.split(".")[3])
end = fourth + count
if end > 254:
    print("This many IP not possible")
for i in range(fourth, end):
    fourth_new=i+1
    new_IP = str(first) + "." + str(sec) + "." + str(third) + "." + str(fourth_new)
    if fourth_new > 254:
        print("invalid IP = ", new_IP)
    else:
        print("valid IP = ", new_IP)


