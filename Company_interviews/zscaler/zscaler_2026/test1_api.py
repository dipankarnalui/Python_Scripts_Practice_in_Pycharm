import requests

url = "https://jsonplaceholder.typicode.com/todos/1"
response=requests.get(url)

print(dir(response))

if response.status_code==200:
    print(response.json())
    print(response.json()["id"])
    print(response.json()["completed"])
else:
    print("error")

