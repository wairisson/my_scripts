import yaml
from rich import print
from jinja2 import Environment, FileSystemLoader
#hosts_yml = yaml.load(open('hosts.yml'), Loader=yaml.FullLoader)
#print(variable_data["asbr01"]["hostname"])
#print(hosts_yml)
#for hosts in hosts_yml:
#    prints(hosts)
#    host_var = hosts+".yml"
#    host_var = list(host_var)
#    print(host_var)
    #for file_host_var in host_var:
    #    print(file_host_var)
#host_file=(hosts["asbr01"]["hostname"])+".yml" # acessando objetos
#print(host_file)

#hosts = yaml.load(open(host_file), Loader=yaml.FullLoader)
#print(host)

#env = Environment(loader = FileSystemLoader("./"), trim_blocks=True, lstrip_blocks=True)
#template = env.get_template("template1.j2")
#print(template)

#print(template.render(variable_data["asbr01"]))
#print(template.render(variable_data["asbr02"]))

groups_yml = yaml.load(open('groups.yml'), Loader=yaml.FullLoader)
#print(variable_data["asbr01"]["hostname"])
#print(groups_yml)
#Especificando host e grupo manualmente
#var22 = {"host":"asbr02", "group":"Routers"}
#print(var22["host"]+".yml")
#print(var22["group"]+".yml")

for x, y in groups_yml.items():
    group_file=(x+".yml")
    groups_vars = yaml.load(open(group_file), Loader=yaml.FullLoader)
#    print("Variáveis de grupo: ", groups_vars)
    for hosts in y:
        host_file = (hosts+".yml")
#        print(host_file)
        host_vars = yaml.load(open(host_file), Loader=yaml.FullLoader)
#        print("Variáveis de host: ",host_vars)
        env = Environment(loader = FileSystemLoader("./"), trim_blocks=True, lstrip_blocks=True)
        template = env.get_template("template1.j2")
#        print(template)
        #Combinando variáveis de grupo e host
        host_vars.update(groups_vars)
#        print(host_vars)
        #renderizando e exibindo
#        print(template.render(host_vars))
        print(template.render(groups_vars))