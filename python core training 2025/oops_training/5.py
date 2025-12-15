class Beta:
    def __lt__(first_obj,second_obj):
        print("Inside __lt__ method")
        print(id(first_obj))
        print(id(second_obj))
        print()
b1 = Beta()
b2 = Beta()

print(id(b1))
print(id(b2))
print()

b1 < b2
