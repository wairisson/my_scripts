import yaml

with open("dict.yml", "r") as file:
    data = yaml.load(file, Loader=yaml.FullLoader)
    print("O conteúdo completo da lista é :", data)
    print("O tipo de dado é: ",type(data))
    var = list(data.items())
    print(var[0])
    print(var[1])
    for i in var[0]:
        print(i)

 #   group_routers = (data["Routers"])
 #   print(group_routers[0])
 #funciona
#    for index in data["Routers"]:
#        print(index)
#        for itens in var:
#            print(itens)





#    var = (data["Routers"])
#    print(var)
#    print(var["hostname"])
#    print("Acessando conteúdo do index 0: ", data["hostname"])
#    print("Acessando conteúdo do index 1: ", data[1])
#    print("Acessando conteúdo do index 3: ", data[2])
