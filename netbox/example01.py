# https://github.com/netbox-community/pynetbox
# Deve ser instalado a library pynetbox usando o link acima

#preencher token a partir https://[your_IP]/user/api-tokens/
import pynetbox
nb = pynetbox.api(
    'https://demo.netbox.dev/',
    token='6e8b4b12ac08298b1f36420e070d57b005ade26b'
)
devices = nb.dcim.devices.all()
for device in devices:

# Exibe o nome do equipamento
    print("Nome do dispositivo: ",device.name, "Status: ", device.status)

# Retorno esperado
# Nome do dispositivo:  RT1 Status:  Active
# Nome do dispositivo:  RT2 Status:  Active
# Nome do dispositivo:  RT3 Status:  Active