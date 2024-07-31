s="today is working day monday"
print(s.index("day"))

#from right side
print(s.rindex("day"))
print(s.count("day"))
print("day" in s)

print(s.find("worked")) #return -1
print(s.index("worked")) #value error