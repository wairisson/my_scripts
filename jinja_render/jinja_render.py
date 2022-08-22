import yaml
from rich import print
from jinja2 import Environment, FileSystemLoader
variable_data = yaml.load(open('hosts.yml'), Loader=yaml.FullLoader)
print(variable_data["RouterA"])

env = Environment(loader = FileSystemLoader("./"), trim_blocks=True, lstrip_blocks=True)
template = env.get_template("template1.j2")
print(template)

print(template.render(variable_data["RouterA"]))
print(template.render(variable_data["RouterB"]))