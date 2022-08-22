from netmiko import ConnectHandler

######### Dictionaries
iosv_sw4 = {
    'device_type': 'cisco_ios',
    'ip': '172.28.129.14',
    'username': 'cisco',
    'password': 'cisco'
}


iosv_sw5 = {
    'device_type': 'cisco_ios',
    'ip': '172.28.129.15',
    'username': 'cisco',
    'password': 'cisco'
}

######### Lists
all_devices = [iosv_sw4, iosv_sw5]



for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    for n in range (2,8):
        print ("Creating VLAN " + str(n))
        config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
        output = net_connect.send_config_set(config_commands)
        print (output) 
