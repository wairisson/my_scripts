#Para fazer o post é necessário gerar um token de permissão
import httpx
import json
from rich import print as rprint


headers = {
    "Accept":"application/yang-data+json",
    "Content-Type":"application/yang-data+json",
    }

my_url = "https://sandbox-iosxe-latest-1.cisco.com/restconf/data/native"

def rest_get_01(url):
    with httpx.Client(verify=False) as client:
        response = client.get(url, headers=headers, auth=("developer", "C1sco12345"))
        #structured_response = json.loads(response.text)
        #return response, structured_response
        #retorna consulta em string
        return response

print("="*50)

results = rest_get_01(url=my_url)
# print normal  retorno <Response [200 OK]>
#rprint(results)
# Retornando a configuração
rprint(results.text)


print("="*50)

my_ospf_url = "https://sandbox-iosxe-latest-1.cisco.com/restconf/data/native/router/router-ospf"
results_ospf = rest_get_01(url=my_ospf_url)
# print normal  retorno <Response [200 OK]>
#rprint(results)
# Retornando a configuração
rprint(results_ospf.text)
