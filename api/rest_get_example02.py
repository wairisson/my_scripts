from urllib import response
from wsgiref import headers
import httpx
import json
from rich import print as rprint

headers = {'accept':'application/json'}
my_url = "http://library.demo.local/api/v1/books?includeISBN=true&sortBy=id"



def pull_info02(url):
    with httpx.Client() as client:
        # Estrutura o dado em json (dict)
        response = json.loads(client.get(url, headers=headers).text)
        # Retorna consulta feito pelo get em string
        return response

results = pull_info02(my_url)
# print normal
rprint(results)
