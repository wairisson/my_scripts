quatro = 4
cinco = 5
dois = 2

soma = quatro + dois
print(soma)  # Resultado: 6

subtracao = quatro - dois
print(subtracao)  # Resultado: 2

multiplicacao = quatro * dois
print(multiplicacao)  # Resultado: 8

divisao = quatro / dois
print(divisao)  # Resultado: 2.0

divisao_interna = quatro // dois
print(divisao_interna)  # Resultado: 2

# Retorna o resto da divisão de ambos operandos.
modulo = quatro % dois
print(modulo)  # Resultado ou resto: 0
modulo = cinco % dois
print(modulo)  # Resultado ou resto: 1

exponenciacao = quatro ** dois
print(exponenciacao)  # Resultado: 16

# Ordem de execução das operações
print(5 * 6 -1) # Resultado: 29, multiplicação executada primeiro
print(5 * (6 -1)) # Resultado: 25, subtração dentro dos parênteses executada primeiro

# Conversão de bases
print(oct(cinco))
print(hex(quatro))
print(bin(dois))

# Boleanos e operadores de comparação
print(cinco == quatro)  # Resultado: False
print(cinco == cinco) # Resultado: True
print(cinco >= cinco) # Resultado: True
print(cinco <= cinco) # Resultado: True
print(cinco != quatro) # Resultado: True
print(cinco > quatro) # Resultado: True
print(cinco < quatro) # Resultado: False
