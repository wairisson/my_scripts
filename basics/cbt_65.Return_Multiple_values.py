# quando uma função retorna múltiplos valores estes são retornados dentro de uma tuple
def math_ops(num1, num2):
    added_result = num1 + num2
    multiplied_result = num1 * num2

    return added_result, multiplied_result

result = math_ops(2,3)
print(f"o tipo é {type(result)}")
print(result)
print(result[0])
print(result[1])

# outra forma de mapear os valores da  tuple direto para duas variáveis é:

x, y = math_ops(7,2)

# apresentando os dados mapeados
print(f"o resultado da multiplicação é {y} e da adição é {x}")