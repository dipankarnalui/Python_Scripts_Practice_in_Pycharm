#Write a program to count the number of capital letters and small letters in a string
sen = "This is A SAMple inpuT"
u_count=0
l_count=0
for e in sen:
    if e.isupper():
        u_count = u_count+1
    if e.islower():
        l_count = l_count + 1
print("Capital Letter = ", u_count)
print("Small Letter = ", l_count)
