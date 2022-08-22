from cmd import IDENTCHARS
from textwrap import indent
import yaml
import json
#hosts file
with open("hosts.yml") as file:
    read_hosts_data = yaml.load(file, Loader=yaml.FullLoader)
    print(json.dumps((read_hosts_data), indent=4))
    print(read_hosts_data["RouterA"]["hostname"])
#    print(groups)
#    for x, y in read_hosts_data.items():
#        print(x)
#        print(y)
#        for i in y:
#            print(read_data[i])
#            print(read_data[i]["bgp_peers"])
#groups file
