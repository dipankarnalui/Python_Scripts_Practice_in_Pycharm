import json

try:
    with open("data.json","r") as f:
        data=json.load(f)
except:
    print("file not found")

print(data)