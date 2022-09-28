#Both * and ** are the operators that perform packing and unpacking in Python.
# The * operator (quite often associated with args) can be used with any
#  iterable (such as a tuple, list and strings), whereas the ** operator,
#  (quite often associated with kwargs) can only be used on dictionaries.


# Função soma 2 paramêtros
def sum02(a, b):
    print(a+b)

sum02(20, 15)

# Problema: Se passarmos 3 parâmetros para uma funcão que espera receber 2 
# haverá erros
# sum02(20, 15, 3)

#Função soma N paramêtros
# Para somar N parâmetro, pode ser passado uma lista como parâmetro para função
# é feito um for para iterar e somar os valores
def sum_n(list01):
    total = 0
    for n in list01:
        total =  total + n
    return total
    

result = sum_n([10,11,2])
print(result)

#Outra forma de tratar múltiplos parâmetros é usando desepacotamento
# a diferença é que não é necessário passar uma lista, os inteiros podem
# ser passados diretamente como parâmetros para função
# Em linhas gerais a função recebe os parâmetros e os armazena na variável
# args que é do tipo tuple
def sum_x(*args):
    total = 0
    print(type(args))
    for n in args:
        total =  total + n
    return total
    

result = sum_x(20,31,2)
print(result)