# Map function itera sobre uma lista passando os valores de forma sucessiva para a função
# objetivo, submeter uma lista de valores a uma funcão

# Cria a lista
my_list = [2, 4, 6, 8, 10]

# cria a função
def squared(num):
    # Retorna numero elevado a 2 
    return num ** 2

# invocando a função passando um parâmentro de forma tradicional
print(squared(10))

# usando a funcão map
new_list = map(squared, my_list)
# Imprimindo o valor de retorno da funcão de forma iterativa sequencial
# 4 prints abaixo retornarão sequencialmente os valores dsa função sendo passado como parametro os valores da lista um valor por vez
print(next(new_list))
print(next(new_list))
print(next(new_list))
print(next(new_list))

# para imprimir todos os valores de uma vez só, o map object resultante da map
# function deve ser convertido para uma lista normal
new_list2 = map(squared, my_list)
print(type(new_list2))
print(new_list2)
#Convertendo e apresentando
print(list(new_list2))


# usando função lambda, 
my_list3 = [3, 5, 7, 9, 11]
new_list3 = list(map(lambda var: var **2, my_list3))
print(new_list3)

# Normaliza strings padronizando primeira letra Maiuscula 
my_list4 = ["wairisson", "Tayná", "nicolas"]
new_list4 = list(map(lambda var: var.capitalize() , my_list4))
print(new_list4)

