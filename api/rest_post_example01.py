#Para fazer o post é necessário gerar um token de permissão
# https://gorest.co.in/
# Este script não funcionou

import httpx
import json
from rich import print as rprint


# incluir token no dict abaixo na key Athorization
headers = {
#    "Accept":"application/json",
#    "Content-Type":"application/json",
    "Authorization":"144e534f498c54d52cb2c432c8f338737064c35031e21a931267ebe5138a939f"
    }

my_url = "https://gorest.co.in/public/v2/users"

payload = {"name":"Tenali Ramakrishna", "gender":"male", "email":"tenali.ramakrishna@15ce.com", "status":"active"}

def post_test_01(url):
    with httpx.Client() as client:
        response = client.post(url, headers=headers, data=payload, )
        structured_response = json.loads(response.text)
        return response, structured_response
        #retorna consulta em string
        #return response.text

results = post_test_01(url=my_url)
# print normal
rprint(results)

