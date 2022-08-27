###########  POP 
# Usado para remover items com base no index, por default remove o último item
list_of_routers = ["R0","R1","R2","R3"]
print(list_of_routers)
# Removendo última posição
list_of_routers.pop()
print(list_of_routers)
#Readicionando última posição
list_of_routers.append("R3")
print(list_of_routers)
# Removendo posição numero 1
list_of_routers.pop(1)
print(list_of_routers)

###########  REMOVE
# Usado para remover items com base conteúdo 
list_of_routers.remove("R2")
print(list_of_routers)

# Adicionando R1
list_of_routers.append("R1")
print(list_of_routers)

# Adicionando R1 após index 0
list_of_routers.insert(1,"R1")
print(list_of_routers)

# neste ponto temos duas ocorrências de R1, o comando abaixo remove a primeira ocorrência de R1
# ou seja a do índex 1
list_of_routers.remove("R1")
print(list_of_routers)


###########  Clear
# remove todos os items de uma lista
list_of_routers.clear()
print(list_of_routers)

