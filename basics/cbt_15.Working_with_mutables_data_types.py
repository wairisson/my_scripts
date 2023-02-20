# Listas permitem armazenamento de múltiplos itens
# mútavel pois é possível alterar seu conteúdo
list = ["vlan1","vlan2","vlan3"]
print(list)
#Exibindo tipo de dado list
print(type(list))
#Exibindo tipo de dado armazenado no index 0 da lista
print(type(list[0]))
print(id(list))
# adicionando vlan4 ao objeto list
list.append('vlan4')
print(list)
print(type(list))
print(id(list))