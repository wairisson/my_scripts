from urllib import response
from wsgiref import headers
import httpx
import json
from rich import print as rprint

headers = {'Accept':'application/json', 'Content-Type':'application/json'}
my_url = "https://gorest.co.in/public/v1/users?"


def pull_info01(url):
    with httpx.Client() as client:
        response = client.get(url, headers=headers)
        #retorna <Response [200 OK]>
        #return response
        #retorna consulta em string
        return response.text

#results = pull_info01(my_url)
# print normal
#print(results)



def pull_info02(url):
    with httpx.Client() as client:
        # Estrutura o dado em json (dict)
        response = json.loads(client.get(url, headers=headers).text)
        # Retorna consulta feito pelo get em string
        return response

results = pull_info02(my_url)
# print normal
rprint(results)

# Acessando a chave Data
rprint(results["data"])
