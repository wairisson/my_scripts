# tuples são lista imutáveis
# execução baseada em tuples resultam em execução mais rápida
# operação mais segura e íntegra pois o conteúdo não muda
vlan_tuple = ("vlan2","vlan3","vlan4","vlan5","vlan5","vlan2")
print(f"O tipo de dado é: {type(vlan_tuple)}")  #O tipo de dado é: <class 'tuple'>
print(vlan_tuple)  # ('vlan2', 'vlan3', 'vlan4', 'vlan5', 'vlan5', 'vlan2')
# tentando adicionar um conteúdo a tuple deve retornar um erro
#vlan_tuple.append("vlan55")
#vlan_tuple[1] = "vlan10"

# mostrando index 1
print(vlan_tuple[1]) #Retorna vlan3

# mostrando quandos itens 
print(len(vlan_tuple)) #Retorna 6

# mostrando valor mínimo
print(min(vlan_tuple)) #Retorna vlan2

# mostrando valor máximo
print(max(vlan_tuple)) #Retorna vlan5

#mostrando quantas ocorrências existem da string vlan5
print(vlan_tuple.count("vlan5")) # Retorna 2

# setando diversas variáveis ao mesmo tempo
(interface, description, ipv4_add) = ("e0/0","Uplink-SW01", "10.0.0.1/24")
print("Interface", interface) #Interface e0/0
print("Description",description) #Description Uplink-SW01
print("ip address",ipv4_add) #ip address 10.0.0.1/24