import requests

response = requests.get("https://api.github.com")

#print(response.status_code)
#print(response.text)
print(response.json())
print(response.headers)
print(response.headers["Content-Type"])

if response.status_code == 200:
    print("Success")

