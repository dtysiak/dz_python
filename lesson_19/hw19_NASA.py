import requests
import random

url = "https://images-api.nasa.gov/search?q=mars&media_type=image"
response = requests.get(url)
data = response.json()
items = data["collection"]["items"]
image_urls = []

for item in items:
    if "links" in item:
        for link in item["links"]:
            image_urls.append(link["href"])

random_photo = random.sample(image_urls, 3)

number = 1
for url in random_photo:
    img_data = requests.get(url).content
    filename = f"version_{number}.jpg"

    with open(filename, "wb") as file:
        file.write(img_data)

    print(filename)
    number = number + 1
