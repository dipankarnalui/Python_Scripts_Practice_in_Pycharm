import requests
import json

response = requests.get("https://httpbin.org/json")

with open("data.json", "w") as f:
    json.dump(response.json(), f, indent=4)

