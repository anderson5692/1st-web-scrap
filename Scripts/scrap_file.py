from bs4 import BeautifulSoup
import requests
import pandas as pd

html_text = requests.get('https://pt.wikipedia.org/wiki/Atletas_mais_medalhados_nos_Jogos_Ol%C3%ADmpicos').text
soup = BeautifulSoup(html_text, 'lxml')
atleta = soup.find_all('table', class_= 'wikitable sortable')
#posição,atleta,pais,ouro,prata,bronze,total
#tupla guarda todos os dados
records = []
for result in results:
    #posição --- date = result.find('strong').text[0:-1] + ', 2017'
    #atleta --- lie = result.contents[1][1:-2]
    # pais --- explanation = result.find('a').text[1:-1]
    # ouro --- url = result.find('a')['href']
    # prata --- records.append((date, lie, explanation, url))
    # bronze
    # total

