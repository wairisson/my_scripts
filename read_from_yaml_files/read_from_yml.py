import yaml
#hosts file
with open("hosts.yml") as file:
    read_hosts_data = yaml.load(file, Loader=yaml.FullLoader)
#    print(read_hosts_data)
#    print(groups)
#    for x, y in read_hosts_data.items():
#        print(x)
#        print(y)
#        for i in y:
#            print(read_data[i])
#            print(read_data[i]["bgp_peers"])
#groups file
with open("groups.yml") as file:
    read_group_data = yaml.load(file, Loader=yaml.FullLoader)
#    print(read_group_data["Groups"])
    groups = (read_group_data["Groups"])
#    print(groups)
    for x, y in groups.items():
#        print(x)
#        print(y)
        for i in y:
#            print(i)
            print("------------------")
            print("------------------")
#            print(read_hosts_data)
#            print(read_hosts_data[i]["bgp_peers"])
            for peers in (read_hosts_data[i]["bgp_peers"]):
                print("neighbor ", peers, "remote-as 100")

