import yaml
from rich import print
from jinja2 import Environment, FileSystemLoader
hosts_yml = yaml.load(open('hosts.yml'), Loader=yaml.FullLoader)
print(hosts_yml["asbr01"]["hostname"])
env = Environment(loader = FileSystemLoader("./"), trim_blocks=True, lstrip_blocks=True)
template = env.get_template("template1.j2")
print(template)

