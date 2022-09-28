# modulos
# Standard - Padrões do python
# Third Party - Instalável via Pip
# Local  -  Criado localmente
# https://docs.python.org/3/library/
#
# Usando módulo rich
#Forma 1
#import rich

#rich.print("[red]Warning[/red]")

#Forma 2
#from rich import print

#print("[red]Warning[/red]")

#Forma 3 - Usando alias, agora basta chamar rp que a função print será chamada
from rich import print as rp
from modules_external import simple_adder as sa

sa(1,4)


rp("[red]Warning[/red]")