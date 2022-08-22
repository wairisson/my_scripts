vendor = "huawei"
firm_ver = "15.7"
model = "ASR9010"

#operador And
print(f"============ Exemplo 1 =============")
if vendor == "Cisco" and firm_ver == "15.6":
    print(f"O equipamento é {vendor} e a versão do firmware é {firm_ver}!!")
else:
    print(f"O equipamento não Cisco é ou a versão do Firmware está incorreta !!")

print(f"============ Exemplo 2 =============")
#operador Or
if vendor == "Cisco" or vendor == "Juniper":
    print(f"O equipamento é um roteador ou swich")
else:
    print(f"O equipamento não é um equipamento de rede")

print(f"============ Exemplo 3 =============")
suported_protocols = ["OSPF", "ISIS", "BGP"]
routing_protocol = "OSPF"
if routing_protocol in suported_protocols:
    print(f"O protocolo {routing_protocol} é suportado.")
else:
    print(f"O protocolo {routing_protocol} não é suportado.")

routing_protocol = input("Informe o protocolo de roteamento: ")
#Usando operador not
if routing_protocol not in suported_protocols:
    print(f"O protocolo {routing_protocol} não é suportado.")
else:
    print(f"O protocolo {routing_protocol} é suportado.")