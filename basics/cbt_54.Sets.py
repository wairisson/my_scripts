# Sets é umtipo de dado não ordenado e mutável com opção de uso do frozen set que é imutável
# Seus itens devem ser únicos, não duplicados
# mac addresses ou IP addresses não devem se duplicados

from site import venv


my_ips = {"192.168.0.1", "192.168.0.2", "192.168.0.3", "192.168.0.4" }
print(type(my_ips))

# Adicionando valores duplicados
# Retorno previso:
# {'192.168.0.3', '192.168.0.2', '192.168.0.1'}
# Note que último valor é mantido
my_ips2 = {"192.168.0.1", "192.168.0.2", "192.168.0.3", "192.168.0.1" }
print(my_ips2)

# adicionando e removendo valores dos sets
my_set = {"cat", "lion", "wolf", "dog"}
print("O ID é",id(my_set))

# Adicionando ao set usando o método add
my_set.add("pantera")
print("O ID é",id(my_set))
print(my_set)

# removendo usando o método remove
my_set.remove("dog")
print(my_set)

# removendo usando o método pop, com o set, o pop não recebe argumento portando
# o comando abaixo deve retornar um erro TypeError: pop() takes no arguments (1 given) 
# o pop faz a remoção de um valor  de forma aleatória
#my_set.pop("lion")
my_set.pop()
print(my_set)

#o pop pode ser usado para tranferir um valor removido para outra variável
vars_popped = my_set.pop()
print(vars_popped)
print(my_set)

# Comparando sets, operação similar a um diff
vrf_a = {"mgmt", "customer_a","customer_b"}
vrf_b = {"customer_a","customer_c", "mgmt"}
print(vrf_a - vrf_b)
print(vrf_b - vrf_a)

# outra forma usando o método difference
print(vrf_a.difference(vrf_b))
print(vrf_b.difference(vrf_a))

# juntando valores usando método union
# apenas valores únicos serão apresentado
print(vrf_a.union(vrf_b))

#imprimindo valores communs usando método intersection
print(vrf_a.intersection(vrf_b))



