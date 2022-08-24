import yaml

with open("list.yml", "r") as file:
    data = yaml.load(file, Loader=yaml.FullLoader)
    print("O conteúdo completo da lista é :", data)
    print("O tipo de dado é: ",type(data))
    print("Acessando conteúdo do index 0: ", data[0])
    print("Acessando conteúdo do index 1: ", data[1])
    print("Acessando conteúdo do index 3: ", data[2])
