#!/usr/bin/env python
# Import dependencies
from napalm import get_network_driver
import json

spine4 = {
    "ipv4_add":"172.28.129.14",
    "os":"ios",
    "type":"switch"
}
spine5 = {
    "ipv4_add":"172.28.129.15",
    "os":"ios",
    "type":"switch"
}
leaf6 = {
    "ipv4_add":"172.28.129.16",
    "os":"ios",
    "type":"switch"
}
leaf7 = {
    "ipv4_add":"172.28.129.17",
    "os":"ios",
    "type":"switch"
}
leaf8 = {
    "ipv4_add":"172.28.129.18",
    "os":"ios",
    "type":"switch"
}
# Group
#spines = [spine4,spine5]
spines = [spine4]
leaves = [leaf6,leaf7,leaf8]
# Commom credentials
credentials = {
    "username":"cisco",
    "password":"cisco"
}

#Test
#print(spines)

for devices in spines:
#Test
#print(devices["ipv4_add"])   
# Define importing for IOS driver
 driver = get_network_driver(devices["os"])
#Ip address and credentials for accessing IOS devices
 device = driver(devices["ipv4_add"], credentials["username"], credentials["password"])
# Function ?? which connect to device using credentials
 device.open()
# display information retrieved using get_facts function # first form
#print(device.get_bgp_neighbors())
# display information retrieved using get_facts function # second form
 print(json.dumps(device.get_bgp_neighbors(), indent=2))
 device.close()

for devices in leaves:
#Test
#print(devices["ipv4_add"])   
# Define importing for IOS driver
 driver = get_network_driver(devices["os"])
#Ip address and credentials for accessing IOS devices
 device = driver(devices["ipv4_add"], credentials["username"], credentials["password"])
# Function ?? which connect to device using credentials
 device.open()
# display information retrieved using get_facts function # first form
#print(device.get_config())
# display information retrieved using get_facts function # second form
 #print(json.dumps(device.get_facts(), indent=4))
 var=(device.get_facts())
 type(var)
 print(var)
 device.close()