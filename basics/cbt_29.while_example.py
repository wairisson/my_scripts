# pode ser um loop infinito
# Define o valor inicial para contador num
num   = 1
while num < 20:
    print(f"O numero {num} é  menor que 20")
    # Incrementa o contador até que ele não seja menor que 10
    num += 1
    # Outra forma
    #num = (num + 1)
print("       =====================")

num2 = 1
while num2 < 5:
    print(f"O numero {num2} é  menor que 5")
    # Incrementa o contador até que ele não seja menor que 10
    if num2 == 4:
        break
    num2 += 1
    # Outra forma
    #num = (num + 1)

username = input("Informe seu nome de usuário: ")
while len(username) < 8:
    print("Erro!! login deve ter mínimo de 8 caracteres!!")
    username = input("Informe seu nome de usuário:")
print("Login criado com sucesso!!")