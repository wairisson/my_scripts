# Atenção, este código não rodou, aparentemente o host está recusando as conexões
import requests

HOST = 'sandbox-iosxe-recomm-1.cisco.com'
USER = 'developer'
PASS = 'C1sco12345'

url = "https://sandbox-iosxe-recomm-1.cisco.com:9443/restconf/data/ietf-interfaces:interfaces"
headers = {'Content-Type': 'application/yang-data+json',
              'Accept': 'application/yang-data+json'}


response = requests.get(url, auth=(USER, PASS), headers=headers, verify=False)


interfaces = response.json()
print(interfaces)
#interfaces['ietf-interfaces:interfaces']['interface'][0]['name']
#'GigabitEthernet1'
#interfaces['ietf-interfaces:interfaces']['interface'][0]['ietf-ip:ipv4']['address'][0]['ip']
#'10.10.20.48'