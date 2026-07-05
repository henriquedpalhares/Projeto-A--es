import requests
import json

acao = input("Qual ação você quer? ").upper()

url = f"https://brapi.dev/api/v2/stocks/quote?symbols={acao}"

response = requests.get(url)

if response.status_code == 200:
    dados = response.json()

    print("Status code:", response.status_code)
    print(json.dumps(dados, indent=4, ensure_ascii=False))

else:
    print("Erro:", response.status_code)