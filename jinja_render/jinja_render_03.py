import yaml
from rich import print
from jinja2 import Environment, FileSystemLoader
hosts_yml = yaml.load(open('hosts.yml'), Loader=yaml.FullLoader)
#print(hosts_yml)
#print("A configuração será renderizada para : ",hosts_yml["asbr01"]["hostname"])
env = Environment(loader = FileSystemLoader("./"), trim_blocks=True, lstrip_blocks=True)
template = env.get_template("template1.j2")
#print(template)

for x, y in hosts_yml.items():
#    print(hosts_yml)
    host_file = (x+".yml")
    host_var = yaml.load(open(host_file), Loader=yaml.FullLoader)
#    print(host_var)
#    print("Configuração para: ",x, "\n")
    print(template.render(host_var))




#itera sobre arquivo hosts com a estrutura abaixo
#asbr02:
#  hostname: asbr02
#  vendor: mikrotik
#for x, y in hosts_yml.items():
#    print("Configuração para: ",x, "\n")
#    print(template.render(y))
#    print("!!!!!!!!!!!!!!!!!!!!!!=============!!!!!!!!!!!!!!!!!!!!!!!", "\n")
