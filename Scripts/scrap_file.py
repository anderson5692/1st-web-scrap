#esse código imprime todos os textos da tabela dos medalhistas

from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://pt.wikipedia.org/wiki/Atletas_mais_medalhados_nos_Jogos_Ol%C3%ADmpicos').text
soup = BeautifulSoup(html_text, 'html.parser')
atleta = soup.find('table', class_= 'wikitable sortable')
#posição,atleta,pais,ouro,prata,bronze,total
for results in atleta:
    nome = atleta.find('tbody')    
print(nome.text)


#esse código abaixo imprimirá um Dataframe Pandas com os 10 maiores medalhistas do mundo
#porém, deve ser executado num jupyter notebook ou Google Colab.

import pandas as pd

df = pd.read_html('https://pt.wikipedia.org/wiki/Atletas_mais_medalhados_nos_Jogos_Ol%C3%ADmpicos')[0][:-59]
df = df.drop(columns=['Modalidade'])
df = df.drop(columns=['Anos'])
df = df.drop(columns=['Jogos'])
df = df.drop(columns=['Sexo'])
df
