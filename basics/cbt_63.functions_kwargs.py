#Both * and ** are the operators that perform packing and unpacking in Python.
# The * operator (quite often associated with args) can be used with any
#  iterable (such as a tuple, list and strings), whereas the ** operator,
#  (quite often associated with kwargs) can only be used on dictionaries.

#Outra forma de tratar múltiplos parâmetros é usando desepacotamento
# a diferença é que não é necessário passar uma lista, os inteiros podem
# ser passados diretamente como parâmetros para função
# Em linhas gerais a função recebe os parâmetros e os armazena na variável
# args que é do tipo tuple
from multiprocessing.sharedctypes import Value


def print_args(*args):
    total = 0
    print(type(args))
    for arg in args:
        print(f"Ther argument passed into this function was {arg}.")

    
print_args(1,2,3,4)

# 3. Keyword argument
# Nesta forma o argumento é especificado junto com sua respectiva variável de forma estática
# Assim a ordem na qual os argumentos são passados é irrelevante
# se chamarmos a função passando os keywords, descomente o trecho abaixo e veja:
# Erro: TypeError: print_args() got an unexpected keyword argument 'num1'
#print_args(num1=1, num2=2, num3=3, num4=4)

#Para receber keyword arguments basta usar **
# o nome do parametro kwargs é definido por convenção mas pode ser outro
def print_kwargs(**kwargs):
    total = 0
    print(type(kwargs))
    # o loop abaixo retornara o nome das variáveis ou as keys
    for arg in kwargs:
        print(f"The argument passed into this function was {arg}.")
    # o loop abaixo retornara o conteúdo key:value do dict
    for arg in kwargs.items():
        print(f"The argument passed into this function was {arg}.")
    # o loop abaixo retornara o conteúdo value do dict
    for arg in kwargs.values():
        print(f"The value passed into this function was {arg}.") 
     # o loop abaixo retornara ambos os valores
    for key, value in kwargs.items():
        print(f"The key is {key} and the value is {value}.")    
print_kwargs(num1=1, num2=2, num3=3, num4=4)

# usando argumentos posicionais e keyword ao mesmo tempo
# CUIDADO!!! argumentos posicionais não podem ser usado após keyword arguments
def print_xargs(a, b, *args, **kwargs):
    total = 0
    print(type(args))
    print(a)
    print(b)
    for arg in args:
        print(f"Ther argument passed into this function was {arg}.")
    for arg in kwargs:
        print(f"Ther argument passed into this function was {kwargs}.")
    
print_xargs(1,2,3,4,name="wairison", lastname="gomes")