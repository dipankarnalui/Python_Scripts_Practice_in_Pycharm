a=[10,29,30,45,10,45,67,10,34,68]
cnt=a.count(10)
print(f"10 is present {cnt} times")
for _ in range(cnt):
    a.remove(10)
print(a)