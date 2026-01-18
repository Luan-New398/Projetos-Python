import requests
import json

url ='https://raw.githubusercontent.com/Luan-New398/Projetos-Python/refs/heads/main/JSONs/Restaurantes.json'

response = requests.get(url)
#print(response)

if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {}
    for item in dados_json:
        nome_restaurante = item['Company']
        if nome_restaurante not in dados_restaurante:
            dados_restaurante[nome_restaurante] = []

        dados_restaurante[nome_restaurante].append({
            "item": item['Item'],
            "price": item['price'],
            "descripition": item['descripition']

        })
    #print(dados_json)
else:
    print(f'O erro foi {response.status_code}')

#print(dados_restaurante['Pizzaria Bella Itália'])

for nome_restaurante, dados in dados_restaurante.items():
    nome_arquivo = f'{nome_restaurante}.json'
    with open(nome_arquivo, 'w') as arquivo_restaurante:
        json.dump(dados,arquivo_restaurante,indent=4)