from bs4 import BeautifulSoup
import requests
import pandas as pd
from lxml import html

html_text = requests.get('https://pt.wikipedia.org/wiki/Atletas_mais_medalhados_nos_Jogos_Ol%C3%ADmpicos').text
soup = BeautifulSoup(html_text, 'lxml')
atleta = soup.find('table', class_= 'wikitable sortable').text
print(atleta)
print('')