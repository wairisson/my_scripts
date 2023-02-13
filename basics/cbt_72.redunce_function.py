# Filter function itera sobre uma lista passando os valores de forma sucessiva para uma função
# objetivo, submeter uma lista de valores a uma funcão

# Cria a lista
my_list = [2, 3, 7, 8, 10]

# cria a função
def checknum(num):
    # Retorna verdade se numero for ímpar
    if num % 2 == 1:
        return True
    else:
        return False

# invocando a função passando um parâmentro de forma tradicional
# retornará true or false
print(checknum(10))
print(checknum(7))


# usando a funcão filter
new_list = filter(checknum, my_list)
# Imprimindo o valor de retorno da funcão de forma iterativa sequencial
# prints abaixo retornarão sequencialmente os valores dsa função sendo passado como parametro os valores da lista um valor por vez
print(next(new_list))
print(next(new_list))
#print(next(new_list))
#print(next(new_list))


my_int_list = ["Gig0/0", "Gig0/0", "Gig0/0", "Fa0/0", "Fa0/1" ]
my_int_gig_list = list(filter(lambda x: x.startswith("Gig"), my_int_list))
print(my_int_gig_list)
