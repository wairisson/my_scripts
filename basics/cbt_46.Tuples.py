# tuples são lista imutáveis
# execução baseada em tuples resultam em execução mais rápida
# operação mais segura e íntegra pois o conteúdo não muda
vlan_tuple = ("vlan2","vlan3","vlan4","vlan5","vlan5","vlan2")
print(f"O tipo de dado é: {type(vlan_tuple)}")
print(vlan_tuple)
# tentando adicionar um conteúdo a tuple deve retornar um erro
#vlan_tuple.append("vlan55")

# mostrando quandos itens 
print(len(vlan_tuple))

# mostrando valor mínimo
print(min(vlan_tuple))

# mostrando valor máximo
print(max(vlan_tuple))

#mostrando quantas ocorrências existem da string vlan5
print(vlan_tuple.count("vlan5"))

