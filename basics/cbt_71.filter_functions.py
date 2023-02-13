from functools import reduce
from unittest import result

# Mesma idéia das funções map e filter, a função reduce recebe um 
# objeto iterável e passa 1 parametro por vez para a função


my_list = [1, 2, 3, 4, 5]

def adder(x, y):
    result = x + y
    return result

# executa o somatório 1 + 2 = 3, 3+3 = 6, 6+4 =10, 10+5 = 15
total = reduce(adder, my_list)
print(total)


def multiplier(x, y):
    result = x * y
    return result

total = reduce(multiplier, my_list)
print(total)

# Itera sobre a lista comparando 2 numeros e vendo qual maior
larger_num = reduce(lambda x, y: x if x > y else y, my_list)
print(f"the larger number in the list is {larger_num}")
