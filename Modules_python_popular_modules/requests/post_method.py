import requests

data = {
    "username": "dipankar",
    "password": "1234"
}

response = requests.post(
    "https://httpbin.org/post",
    data=data
)

print(response.text)

