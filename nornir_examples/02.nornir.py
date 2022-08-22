# Initializing objects for later use
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")
# filtering objects to simplify output
nr = nr.filter(site="site_a", role="spine")

from nornir.core.task import Task, Result

def hello_world(task: Task) -> Result:
    return Result(
        host=task.host,
        result=f"{task.host.name} says hello world!"
    )

result = nr.run(task=hello_world)
print_result(result)