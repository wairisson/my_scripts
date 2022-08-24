# Initializing objects for later use
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get
nr = InitNornir(config_file="config.yaml")
# filtering objects to simplify output
nr = nr.filter(site="site_a", role="spine")


result = nr.run(
    task=napalm_get, getters=["facts","interfaces"]
    )
print_result(result)