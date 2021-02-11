from bs4 import BeautifulSoup

import requests

html = requests.get("https://www.climatempo.com.br/").content

soup = BeautifulSoup(html, 'html.parser')

print(soup.prettify())

medalhas = soup.find(class_="_margin-r-20")
print(medalhas.string)


