import requests

BASE_URL = "http://127.0.0.1:8080/delete/test.jpg"

response = requests.delete(BASE_URL)

print(response.status_code)
print(response.json())