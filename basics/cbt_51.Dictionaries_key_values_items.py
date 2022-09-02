device_info = {
    "layer":"distribution",
    "ASN": 65001,
    "plataform":"cisco_iosxe",
    "version": 15.6,
    "serial":"ASD3322"
}

print("\n","========START=========","\n")
print(device_info)
print("\n","========+++(Usando o método keys)++++=======","\n")
# útil para acessar apenas as chaves do dict
print(device_info.keys())
print(type(device_info.keys()))

print("\n","========+++++++=======","\n")
#
print("\n","========+++(Convertendo dict para para list)++++=======","\n")
# Cria uma lista composta apenas pelas keys
list_keys_device_info = list(device_info.keys())
print(type(list_keys_device_info))
print(list_keys_device_info)
for key in list_keys_device_info:
    print("A chave é: ", key)
print("\n","========+++++++=======","\n")

print("\n","========+++(Usando o método values e convertendo para list)++++=======","\n")
# útil para acessar apenas os values do dict
print(device_info.values())
print(type(device_info.values()))
list_values_device_info = list(device_info.values())
print(list_values_device_info)
print(type(list_values_device_info))
for value in list_values_device_info:
    print("O valor é: ", value)
print("\n","========+++++++=======","\n")


print("\n","========+++(Usando o método items e convertendo para list)++++=======","\n")
# O método items converte para uma dicionario de tuples
print(device_info.items())
print(type(device_info.items()))
list_items_device_info = list(device_info.items())
print(list_items_device_info)
print("\n","========+++Acessando index 0 da lista++++=======","\n")
print(list_items_device_info[0])
print("\n","========+++Acessando staticamente indexes da tuple 0++++=======","\n")
print(list_items_device_info[0][0])
print(list_items_device_info[0][1])
print("\n","========++++Exibindo o tipo da lista+++=======","\n")
print(type(list_items_device_info))
print("\n","========++++Iterando sobre os indexes da lista+++=======","\n")
for item in list_items_device_info:
    print("O valor é: ", item, "e o tipo é: ", type(item))
    for i in item:
        print("Acessando conteúdo da tuple: ", i)
print("\n","========+++++++=======","\n")