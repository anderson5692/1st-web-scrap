from bs4 import BeautifulSoup
import requests
import pandas as pd
from lxml import html

html_text = requests.get('https://pt.wikipedia.org/wiki/Atletas_mais_medalhados_nos_Jogos_Ol%C3%ADmpicos').text
soup = BeautifulSoup(html_text, 'lxml')
atleta = soup.find_all('table', class_= 'wikitable sortable')
position = [p.get_text() for p in headerSort.select(".th .title")]
nome = [n.get_text() for n in headerSort.select(".th .title")]
country = [c.get_text() for c in headerSort.select(".th .title")]

print(position)
print(nome)
print(country)
