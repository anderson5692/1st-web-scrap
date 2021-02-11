from bs4 import BeautifulSoup

import requests

html = requests.get("https://www.climatempo.com.br/").content

soup = BeautifulSoup(html, 'html.parser')

print(soup.prettify())

