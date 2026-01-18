from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/hello')
def hello_world():
    '''

    Endpoint para teste

    '''

    return {'Hello':'World'}
   

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    '''
    Endpoind para mostrar os cardápios dos restaurantes
    '''
    url ='https://raw.githubusercontent.com/Luan-New398/Projetos-Python/refs/heads/main/JSONs/Restaurantes.json'

    response = requests.get(url)

    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return {'Dados':dados_json}
        
        dados_restaurante = []
        for item in dados_json:
            if item['Company'] == restaurante:
                dados_restaurante.append({
                    "item": item['Item'],
                    "price": item['price'],
                    "descripition": item['descripition']
                })
        return {'Restaurante':restaurante,'Cardapio':dados_restaurante}
    else:
        print(f'O erro foi {response.status_code} - {response.text}')
