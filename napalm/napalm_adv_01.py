import napalm
from tabulate import tabulate
 
def main():
 
    driver_ios = napalm.get_network_driver("ios")
    driver_iosxr = napalm.get_network_driver("iosxr")
 
    device_list = [["172.28.129.14","ios", "switch"],["172.28.129.15","ios", "switch"]]
 
    network_devices = []
    for device in device_list:
        if device[1] == "ios":
            network_devices.append(
                            driver_ios(
                            hostname = device[0],
                            username = "cisco",
                            password = "cisco"
                            )
                              )
        elif device[1] == "iosxr":
            network_devices.append(
                            driver_iosxr(
                            hostname = device[0],
                            username = "xxx",
                            password = "xxx"
                            )
                              )
 
    devices_table = [["hostname", "vendor", "model", "uptime", "serial_number"]]
 
    for device in network_devices:
        print("Connecting to {} ...".format(device.hostname))
        device.open()
 
        print("Getting device facts")
        device_facts = device.get_facts()
        print(device_facts)

        devices_table.append([device_facts["hostname"],
                              device_facts["vendor"],
                              device_facts["model"],
                              device_facts["uptime"],
                              device_facts["serial_number"]
                              ])
 
        device.close()
        print("Done.")
   # print(tabulate(devices_table, headers="firstrow"))
 
if __name__ == '__main__':
    main()