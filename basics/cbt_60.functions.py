#Funções
# Passando argumentos
# 1. Argumentos posicionais
# - Argumentos passados são mapeados posicionalmente para os argumento da função
def device_login(username, hostname, plataform):
    print(f"ssh {username}@{hostname}")
    if plataform == "cisco":
        print("enable\nconfigure terminal\nshow running-config\n")

device_login("wairisson","10.0.0.1","cisco")
#
#
# 2. Default argument
# No exemplo abaixo basta informar o valor default para variável dentro da linha da 
#definição da função
def device_login2(username, hostname, plataform="huawei"):
    print(f"ssh {username}@{hostname}")
    if plataform == "cisco":
        print("enable\nconfigure terminal\nshow running-config\n")
    elif plataform == "huawei":
        print("system view\ndisplay current-configuration\n")
    else:
        print(f"Plataform {plataform} is unknown")

#Note que não está sendo informado parâmetro para plataforma
device_login2("wairisson","10.0.0.1")
device_login2("wairisson","10.0.0.1","junos")
#
# 3. Keyword argument
# Nesta forma o argumento é especificado junto com sua respectiva variável de forma estática
# Assim a ordem na qual os argumentos são passados é irrelevante
device_login2(plataform="sros",hostname="10.0.0.1",username="wairisson")

# observação importante, um argumento posicional não pode ser usado após 
# um keywork argument
# Exemplo invocar a funcão da forma abaixo seria incorreto
device_login2(username="wairisson","10.0.0.1","junos")
#Contudo a construção abaixo seria válida
device_login2("wairisson",hostname="10.0.0.1",plataform="junos")