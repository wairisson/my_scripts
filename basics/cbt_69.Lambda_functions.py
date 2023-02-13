# Funções Lambda
# Podem ser named ou anonymous
# Funcões regulares retornam none por default
# Fuções lambda sempre retornam pelo menos um valor
# objetivo das funcões lambda é deixar o código mais simples e readble
def regular_function(num1, num2):
    result =  num1 + num2
    return result

answer = regular_function(12, 13)
print(answer)

# Usando função lambda
# estrutura :lambda + parametros + operação
adder = lambda num1, num2: num1 + num2
print(adder(23, 24))

# No exemplo abaixo definimos um valor default para varíavel y que será usado caso o usuário não informe um valor
exponential = lambda x, y=2: x**y
print(exponential(6))
print(exponential(6, 3))

check_number = lambda x: "The number is greater than 10"  if x > 10 else "The number is not greater than 10"
print(check_number(7))
print(check_number(12))