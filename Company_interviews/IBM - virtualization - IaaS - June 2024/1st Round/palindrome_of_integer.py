num=12121
store=0
while num != 0:
    num_len = len(str(num))
    print(num_len)
    last = num % 10
    print("last = ",last)
    store = store + last + 10**num_len
    print("store = ",store)
    num=int(num/10)
    print(num)