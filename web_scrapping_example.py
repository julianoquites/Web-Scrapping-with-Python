import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# URL do Mercado Livre
url = 'https://www.mercadolivre.com.br/ofertas#c_id=/home/promotions-recommendations&c_uid=1baf6fec-4e6b-4f28-b7ce-ed69bd603ccb'

# Fazendo a solicitação HTTP
response = requests.get(url)

# Analisando o HTML da página
soup = BeautifulSoup(response.text, 'html.parser')

# Encontrando os elementos que contêm informações sobre produtos
product_elements = soup.find_all('div', class_='section_promotions_web')

# Listas para armazenar nomes e preços dos produtos
product_names = []
product_prices = []

# Extraindo nomes e preços dos produtos
for name in soup.find_all('p', class_='promotion-item__title'):
    name = name.text.strip()
    product_names.append(name)

for price in soup.find_all('span', class_='andes-money-amount andes-money-amount--cents-superscript'):
    price = price.text.strip()
    product_prices.append(price)

# Criando um DataFrame com as informações coletadas
data = {'Nome do Produto': product_names, 'Preço': product_prices, 'Data de Consulta': [datetime.today().strftime('%d-%m-%Y')] * len(product_names)}
df = pd.DataFrame(data)

# Exibindo o DataFrame
print(df)

# Salvando o DataFrame em um arquivo JSON
df.to_json('output.json', orient='records', force_ascii=False, indent=2)