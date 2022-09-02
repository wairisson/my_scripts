# Dictionaries é uma lista não ordenada Key: Value
# Diferenças entre lista e dicionário 
# lista ordenada, dict não ordenada
# lista o acesso a lista é feito via index [x]
# dict o acesso é feito via Key
# Ambos são mutáveis, porém no dict a key deve ser imutable
# Nos dict strings, numbers e tuple podem ser key, listas não podem ser key

print("\n","==============","\n")
# Exemplo abaixo a key last_name está repetida e irá exibir o último valor setado
dict_personal_data = {
    "first_name":"Wairisson",
    "last_name":"Gomes",
    "age": 38,
    "married": True,
    "have_child":True,
    "last_name":"Milhomem"}
print(dict_personal_data)
print("\n","==============","\n")
# Usando o método get
# Diferença: caso a chave invocada não exista ele retorna o valor "None" 
# se o print for usado e a chave não existir um erro de chave é retornado
print("Teste de uso do método get:: ",dict_personal_data.get("first_name"))
print("Teste erro no uso do método get:: ",dict_personal_data.get("middle_name", "This key does not exist"))
# lista de dicts [{},{}]
# No caso abaixo temos uma lista com dois dicts como objetos da lista
print("\n","==============","\n")
# Exemplo abaixo a key last_name está repetida e irá exibir o último valor setado
list_personal_data = [
    {"first_name":"Wairisson",
    "last_name":"Gomes",
    "age": 38},
    {"first_name":"Tayná",
    "last_name":"Barros",
    "age": 30}
    ]
print(list_personal_data)
print("\n","==============","\n")

print(list_personal_data[0])
print("\n","==============","\n")


print(list_personal_data[1])
print("\n","==============","\n")

devices = {
    "hostname":"sp-spo-border01",
    "mgmt_ipv4":"10.0.0.1",
    "vendor":"cisco",
    "model":"ASR1004",
    "prod":True
}

print(f"O Tipo do dict devices é {type(devices)}")
print(f"O ID do dict devices é {id(devices)}")
print(f"O conteúdo atual do dict devices é: {devices}")
print("\n","==============","\n")
# Adicionando dados ao dict
devices["plataform"] = "cisco_ios"
print(f"O conteúdo atual do dict devices é: {devices}")
print(f"O ID do dict devices é {id(devices)}")
print("\n","==============","\n")

# acessando conteúdo do dict
print(f"O do vendor do equipamento", devices["hostname"], "é", devices["vendor"])

#usando listas de dicts
devices = [
    {"hostname":"sp-spo-border01",
    "mgmt_ipv4":"10.0.0.1",
    "vendor":"cisco",
    "model":"ASR1004",
    "prod":True},
    {"hostname":"sp-spo-border02",
    "mgmt_ipv4":"10.0.0.2",
    "vendor":"juniper",
    "model":"MX80",
    "prod":False}
    ]

print(type(devices))

# Acessando o primeiro dict da lista
print(devices[0])

# Iterando sobre a lista de dicts
for item in devices:
    if item["prod"]:
        print("Os equipamentos ativos são: ")
        print(item["vendor"],item["hostname"])

print("\n","==============","\n")



############# Removendo items

print("\n","==============","\n")
# Exemplo abaixo a key last_name está repetida e irá exibir o último valor setado
dict_personal_data = {
    "first_name":"Wairisson",
    "last_name":"Gomes",
    "age": 38,
    "married": True,
    "have_child":True} 
print(dict_personal_data)
print("\n","==============","\n")

# Removendo items
# usando comando del
del dict_personal_data["have_child"]
print(dict_personal_data)
print("\n","==============","\n")

# usando metodo pop
dict_personal_data.pop("married")
print(dict_personal_data)
print("\n","==============","\n")
# removendo a key age ao mesmo tempo atribuindo seu valor para outra var
new_age = dict_personal_data.pop("age")
print(dict_personal_data)
print("New Age content: ", new_age)
# Definindo uma mensagem customizada de erro ao remover uma chave já removida
# primeiro sem a mensagem
#print(dict_personal_data.pop("married"))
# com mensagem
print(dict_personal_data.pop("married","Erro a chave não existe!!"))



