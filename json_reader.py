import json

# Caminho para o arquivo JSON
json_file = 'output.json'

# Lendo o conteúdo do arquivo JSON com a codificação 'utf-8'
with open(json_file, 'r', encoding='utf-8') as arquivo:
    dados_json = json.load(arquivo)

# Exibindo os dados lidos
print(dados_json)