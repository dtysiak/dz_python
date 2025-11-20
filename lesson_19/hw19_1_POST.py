import requests

BASE_URL = "http://127.0.0.1:8080/upload"

with open("test.jpg", "rb") as file:
    files = {"image": file}
    response = requests.post(BASE_URL, files=files)

print(response.status_code)
print(response.json())
