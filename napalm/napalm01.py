#!/usr/bin/env python
# Import dependencies
from napalm import get_network_driver
import json

# Define importing for IOS driver
driver = get_network_driver('ios')

#Ip address and credentials for accessing IOS devices
device = driver('172.28.129.14', 'cisco', 'cisco')

# Function ?? which connect to device using credentials
device.open()


# display information retrieved using get_facts function # first form
#print(device.get_facts())
#print("#################################################")
# display information retrieved using get_facts function # second form
# sort_keys=True ordena os resultados
#ios_output = (json.dumps(device.get_facts(), indent=4))
#print(ios_output)
##
#acessando dados 
ios_output = device.get_facts()
print(ios_output["vendor"],ios_output["uptime"])

#ios_output = (json.dumps(device.get_interfaces(), indent=4))
#print(ios_output)

#ios_output = (json.dumps(device.get_interfaces_counters(), sort_keys=True, indent=4))
#print(ios_output)

#ios_output = (json.dumps(device.get_mac_address_table(), indent=4))
#print(ios_output)
device.close()