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
#print(device.get_bgp_neighbors())

# display information retrieved using get_facts function # second form
print(json.dumps(device.get_bgp_neighbors(), indent=2))
device.close()