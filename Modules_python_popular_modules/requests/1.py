import requests

response=requests.get('http://httpbin.org/ip')
print(response.status_code)

print(response.text)
