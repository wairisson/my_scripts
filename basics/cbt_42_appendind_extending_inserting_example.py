###########  APPEND
# O append é usado para adicionar apenas 1 item novo a uma lista
list_of_routers = ["R1","R2","R3","R4"]
print(list_of_routers)
# addicionando elementos a lista
list_of_routers.append("R5")
print(list_of_routers)
# executando novamente adicionará novamente, não substituirá
list_of_routers.append("R5")
print(list_of_routers)
list_of_switches = ["ASW1","ASW2"]

###########  EXTEND
# o extend é usado para adicionar vários items
# adicionando uma lista ao conteúdo de outra, neste caso o python fará um for adicionando item por item da lista list_of_switches a lista list_of_routers
# para usar o extend o objeto deve ser iterável, ou seja, uma lista
list_of_routers.extend(list_of_switches) 
print(list_of_routers)

###########  INSERT
# o insert é usado para adicionar items em posição específica

list_of_switches.insert(1, "DSW1") 
print(list_of_switches)
list_of_switches.insert(0, "DSW0") 
print(list_of_switches)
list_of_switches.insert(-1, "DSW10") 
print(list_of_switches)

###########  ITERANDO
list_of_ASW = []
for items in list_of_routers:
    if "ASW" in items:
        print(f"Os switches de acesso são são: {items}")
        list_of_ASW.append(items)
    else:
        print(f"Os routers são: {items}")
print(list_of_ASW)

# A forma abaixo vai iterar sobre a string TESTE letra por letra, cada letra será tratada como um objeto
#var =  "TESTE"
#for items in var:
 #   print(items)

#resultado:
# T
# E
# S
# T
# E

# Solução de contorno
#var =  "TESTE"
#list_var = [var]
#for items in list_var:
#    print(items)
#resultado:
# TESTE


