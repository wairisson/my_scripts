###  FUNCIONA

# Initializing objects for later use
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get
from nornir_netmiko import netmiko_send_config, netmiko_save_config, netmiko_send_command
from nornir_jinja2.plugins.tasks import template_file

nr = InitNornir(config_file="config.yaml")
# filtering objects to simplify output
nr = nr.filter(site="site_a", role="spine")



def add_vlan(task):
    cmd = task.run(task=template_file,
                   name="Generating template",
                   template="add_vlans.j2",
                   path="./templates/",
                   vlan_id="620",
                   vlan_name="vlan-620"
                   )
    teste = cmd.result
#    print(teste)
    task.host["config"] = cmd.result
    configuration = teste.splitlines()
    print(configuration)
    task.run(task=netmiko_send_config,
             name="Sending configuration",
             config_commands=configuration)
    task.run(task=netmiko_save_config,
             name="Saving configuration",
             cmd="write memory")
    task.run(task=netmiko_send_command, name="Show Vlans", command_string="show ip int brief")

r = nr.run(task=add_vlan)
print_result(r)