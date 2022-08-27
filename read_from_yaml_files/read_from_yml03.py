import yaml
from rich import print
from jinja2 import Environment, FileSystemLoader

#hosts file
with open("read_from_yml03.yml") as file:
    data = yaml.load(file, Loader=yaml.FullLoader)
#    print(data["interface"])

#carregando o template
env = Environment(loader = FileSystemLoader("./"), trim_blocks=True, lstrip_blocks=True)
template = env.get_template("read_from_yml03.j2")
print(template)

# renderizando
print(template.render(data))