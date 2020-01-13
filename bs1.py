from bs4 import BeautifulSoup
import requests


url = 'https://pizza.od.ua/menu/pizza'
response = requests.get(url)
print(response.status_code)
contents = response.text

soup = BeautifulSoup(contents, 'lxml')

pizza_names = []
for name in soup.findAll("div", {"class": "catalog-name"}):
    pizza_names.append(name.text)
print(pizza_names)

pizza_price = []
for price in soup.findAll("div", {"class": "bx_price price"}):
    pizza_price.append(price.text)
print(pizza_price)

pizza_photo = []
for photo in soup.findAll("img"):
    pizza_photo.append(photo['src'])
print(pizza_photo)

pizza_description = []
for description in soup.findAll("p"):
    pizza_description.append(description.text)
pizza_description = pizza_description[1:-5]
print(pizza_description)

pizzas_zipped = zip(pizza_names, pizza_price, pizza_photo, pizza_description)
pizzas_parced = list(pizzas_zipped)
print(pizzas_parced)
