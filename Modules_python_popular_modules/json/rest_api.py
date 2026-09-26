import requests
response = requests.get("https://api.example.com/users")
data = response.json()
print(data)

