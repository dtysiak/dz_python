import requests

BASE_URL = "http://127.0.0.1:8080/image/test.jpg"

headers = {"Content-Type": "text"}
response = requests.get(BASE_URL, headers=headers)

print(response.status_code)
print(response.json())