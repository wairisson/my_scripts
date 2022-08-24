import yaml

#with open("Routers.yml", "r") as file:
#    data = yaml.load(file, Loader=yaml.FullLoader)
#    print("O conteúdo completo do dict é :", data)
#    for x, y in data.items():
#        print(y)
#        for key in y:
#            print(key)

with open("dict.yml", "r") as file:
    data = yaml.load(file, Loader=yaml.FullLoader)
#    print("O conteúdo completo do dict é :", data)
#    print("O tipo de dado é: ",type(data))
    for x, y in data.items():
        print(y)
        for items_y in y:
            print(items_y + ":",y[items_y])
#        filename_y=y+".yml"
#        print(filename_y)
#        for itens_y in y:
#            print(itens_y)
#            with open((filename_y), "r") as file_y:
#                data_y = yaml.load(file_y, Loader=yaml.FullLoader)
#                print("O conteúdo completo do dict é :", data_y)

#        filename=x+".yml"
#        print(filename)
#        with open((filename), "r") as file2:
#            data2 = yaml.load(file2, Loader=yaml.FullLoader)
#            print("O conteúdo completo do dict é :", data2)