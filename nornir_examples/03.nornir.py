# Initializing objects for later use
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir.plugins.tasks.networking import netmiko_send_config
nr = InitNornir(config_file="config.yaml")
# filtering objects to simplify output
nr = nr.filter(site="site_a", role="spine")


#result = nr.run(
#    task=napalm_get, getters=["facts","interfaces"]
#    )
#print_result(result)