R1 = {
    "hostname" : "R1",
    "vendor" : "Cisco"
}

R2 = {
    "hostname":"R2",
    "vendor":"Huawei"
}

SW1 = {
    "hostname":"Sw1",
    "vendor":"Juniper"
}

SW2 = {
    "hostname":"Sw2",
    "vendor":"Arista"
}

device_list01 = [R1, R2, SW1, SW2]
for device in device_list01:
    print(device["hostname"],device["vendor"],"Tipo de dado:",type(device))
print("\n","          ===========","\n")
device_list02 = ["R1", "R2", "SW1", "SW2"]
for device in device_list02:
    print(device,"Tipo de dado:",type(device))

print("\n","          ===========","\n")

# Usando o continue
# Note que o R2 não será exido, ou seja não será processado
device_list03 = ["R1", "R2", "SW1", "SW2"]
for device in device_list03:
    if device == "R2":
        continue
    print(device)

print("\n","          ===========","\n")


# No exemplo abaixo dispositivos que iniciam com R não serão exibidos
for device in device_list03:
    if device.startswith("R"):
        continue
    print(device)