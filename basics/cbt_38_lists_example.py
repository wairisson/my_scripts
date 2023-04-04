# Listas permitem armazenamento de múltiplos itens de multiplos tipos
# - mútavel
# Ordenada
# quantidade de itens em lista depende da quantidade de memória
# list is a collection of elements, but each element is a scalar.

list1 = ["vlan5","vlan6","vlan7"]
list2 = ["vlan15","vlan16","vlan17"]
list3 = list1
# armazena tipos de dados diferentes
list4 = [4,"4",4.4,"quatro",list1]
#exibindo tipo de dados dentro da lista

for item in list4:
    print(type(item))

# Codigo for acima faz o mesmo que o código abaixo
# Acessando conteúdo das listas usando os index
print(type(list4[0]))
print(type(list4[1]))
print(type(list4[2]))
print(type(list4[3]))
print(type(list4[4]))
print(f" ====== acessando o último item da lista 4 usando -1:  {list4[-1]}","\n")
print(f" ====== acessando o penúltimo item da lista 4 usando -2 : {list4[-2]}","\n")



print(f"Conteúdo da lista 1: {list1}")
print(f"Conteúdo da lista 2: {list2}")
print(f"Conteúdo da lista 2: {list3}")
print(f"Conteúdo da lista 2: {list4}")

if list1 == list2:
    print("As listas 1 e 2 são iguais !")
else:
    print("As listas 1 e 2 são diferentes.")

if list1 == list3:
    print("As listas 1 e 3 são iguais !")
else:
    print("As listas 1 e 3 são diferentes.")

# cria uma lista de listas
list_of_list1 = [list1, list2, list3, list4]
#iterando sobre lista de lista
for list in list_of_list1:
#    print(f"O conteúdo da lista de listas é: {list}")
    print(f"{list}")
    for content in list:
        print(f"O conteúdo da lista interna é {content} do tipo {type(content)}")


# acessando lista de lista
print("Acessando lista de lista")
print(type(list_of_list1[3]))
print(list_of_list1[0])
print(list_of_list1[1])
print(list_of_list1[2])
print(list_of_list1[3])
# acessando conteúdo da lista dentro da lista
print("Acessando conteúdo de uma lista dentro de uma outra lista")
print(type(list_of_list1[3][0]))
print(list_of_list1[3][0])

# Usando slices, neste caso sa sintaxe [i:f] i será inclusivo e f será exclusivo
list5  = ["Pos0","Pos1","Pos2","Pos3","Pos4"]
print(f"Exibindo posições de 0 a 3: {list5[0:4]}")
print(f"Exibindo posições de 0 a 4: {list5[0:5]}")
print(f"Exibindo posições de 2 em diante: {list5[2:]}")
print(f"Exibindo posições até a posição  3 em diante: {list5[:4]}")
print(f"Exibindo posições de 0 a 4 de 2 em 2: {list5[0:5:2]}")

# Métodos
print("\n")
print("######################### - Método append -###########################\n")
print("\n")
# append, adiciona objetos a lista
print(list1) # Retorna ['vlan5', 'vlan6', 'vlan7']
list1.append("vlan8")
print(list1) # Retorna ['vlan5', 'vlan6', 'vlan7', 'vlan8']
print("\n")
print("######################### - Método append -###########################\n")
print("\n")


print("\n")
print("######################### - Método insert -###########################\n")
print("\n")
# insert, adiciona objetos a lista em um índice específico
print(list1) # Retorna ['vlan5', 'vlan6', 'vlan7']
list1.insert(0, "vlan99")
print(list1) # Retorna ['vlan5', 'vlan6', 'vlan7', 'vlan8']
print("\n")
print("######################### - Método insert -###########################\n")
print("\n")

print("\n")
print("######################### - Método copy -###########################\n")
print("\n")
list1.copy()
print("\n")
print("######################### - Método copy -###########################\n")
print("\n")

print("\n")
print("######################### - Método clear -###########################\n")
print("\n")
# clear, remove todos os objetos da lista
list1.clear()
print(list1) # Retorna [] 
print("\n")
print("######################### - Método clear -###########################\n")
print("\n")
# usando índices negativos retornam últimas posições
numbers = [111, 7, 2, 1]
print(numbers[-1]) # retorna 1, que é o indice 3


#### Hands on
hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.

# Step 2: write a line of code that removes the last element from the list.

# Step 3: write a line of code that prints the length of the existing list.


####


my_list = []  # Creating an empty list.

for i in range(5):
    my_list.append(i + 1)

print(my_list)

print("\n")
print("######################### - Somando objetos da lista -###########################\n")
print("\n")
my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)