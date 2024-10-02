import sys

print(sys.argv)

if len(sys.argv) < 4:
    print("Enter Min 3 arguments")
else:
    print(sys.argv[3])