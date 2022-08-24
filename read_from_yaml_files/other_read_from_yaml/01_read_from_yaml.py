import yaml
from yaml.loader import SafeLoader
import sys
from pathlib import Path
variables_file = Path(sys.argv[1])

with open(variables_file, "r") as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
#    print(data)
    hosts_dict=(data["hosts"])
    spine_groups_dict=(data["spine"])
    print(hosts_dict)
    print(spine_groups_dict)

#    for values in hosts_dict:
#        print(values["hostname"])
        #print(data)
#print(data)
#print("O tipo de dado é: ",type(data))

#driver = get_network_driver(devices["os"])

#device = driver(devices["ipv4_add"],