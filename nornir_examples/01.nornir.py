from nornir import InitNornir
nr = InitNornir(config_file="config.yaml")

print(nr.inventory.hosts)
print(nr.inventory.hosts["spine4"])
print(nr.inventory.groups)
print(nr.inventory.groups["cisco_ios"])