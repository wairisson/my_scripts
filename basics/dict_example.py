sw02 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.82',
    'username': 'david',
    'password': 'cisco',
}

print("O tipo de dado é: ", type(sw02))
print("Exibindo o dict inteiro: ",sw02)
print("Exibindo o conteúdo da chave device_type: ",sw02["device_type"])

sw03 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.83',
    'username': 'david',
    'password': 'cisco',
}

print("O tipo de dado é: ", type(sw03))
print("Exibindo o dict inteiro: ",sw03)
print("Exibindo o conteúdo da chave device_type: ",sw03["device_type"])

all_devices  = [sw02, sw03]

print("Exibindo todos os dispositivos : ", all_devices)
print("Exibindo conteudo de um dict dentro de uma lista : ", all_devices[0]["device_type"])


