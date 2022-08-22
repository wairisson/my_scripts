from netmiko import ConnectHandler

######### Dictionaries
sw4 = {
    'device_type': 'cisco_ios',
    'ip': '172.28.129.14',
    'username': 'cisco',
    'password': 'cisco'
}


sw5 = {
    'device_type': 'cisco_ios',
    'ip': '172.28.129.15',
    'username': 'cisco',
    'password': 'cisco'
}

sw6 = {
    'device_type': 'cisco_ios',
    'ip': '172.28.129.16',
    'username': 'cisco',
    'password': 'cisco'
}


sw7 = {
    'device_type': 'cisco_ios',
    'ip': '172.28.129.17',
    'username': 'cisco',
    'password': 'cisco'
}
sw8 = {
    'device_type': 'cisco_ios',
    'ip': '172.28.129.18',
    'username': 'cisco',
    'password': 'cisco'
}



######### Lists
spine = [sw4, sw5]
leaf = [sw6, sw7, sw8]
leafnames = ["sw9", "sw10", "sw11"]
# with open('./group_vars/spine_switches.txt') as f:
#     lines = f.read().splitlines()
# # Exibe as linhas do arquivo
# print (lines)
# 
# for devices in spine:
#     net_connect = ConnectHandler(**devices)
#     output = net_connect.send_config_set(lines)
#     print (output)
# 
# with open('./group_vars/leaf_switches.txt') as f:
#     lines = f.read().splitlines()
# # Exibe as linhas do arquivo
# print (lines)
# 
# 
# for devices in leaf:
#     net_connect = ConnectHandler(**devices)
#     output = net_connect.send_config_set(lines)
#     print (output)

print (leafnames)
#for devices in leaf:
#    print ('./host_vars/spine_switches.txt') 
 #   print (devices)
