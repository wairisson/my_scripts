### NAO FUNCIONA

# Initializing objects for later use
from nornir import InitNornir
from nornir_utils.plugins.tasks.data import load_yaml
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get
from nornir_netmiko import netmiko_send_config, netmiko_save_config, netmiko_send_command
from nornir_jinja2.plugins.tasks import template_file

nr = InitNornir(config_file="config.yaml")
# filtering objects to simplify output
nr = nr.filter(site="site_a", role="spine")


def load_vars(task):
    data = task.run(task=load_yaml, name="Pulling Hosts Vars", file=f"./host_vars/{task.host}.yml")
    task.host["facts"] = data.result
    push_vlans(task)
#    host = task.host
#    print(host)

def push_vlans(task):
    data = task.run(task=load_yaml, name="Pulling Hosts Vars", file=f"./host_vars/{task.host}.yml")
    task.host["facts"] = data.result
#    push_vlans(task)
#    print(vlan_id)
    i = task.run(task=template_file, name="Bulding Configuration", template="add_vlans.j2",path="./templates")
    task.host["vlan_add"] = i.result
    vlan_output = task.host["vlan_add"]
#    vlan_send = vlan_output.splitlines()
    task.run(task=netmiko_send_config, name="Pushing Configuration",config_commands=vlan_send)
    task.run(
        task=netmiko_send_command,
        name="Verifing VLAN Creation",
        command_srings="show vlans"

    )

results = nr.run(task=push_vlans)
print_result(results)