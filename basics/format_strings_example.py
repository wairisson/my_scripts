#old way
name = input("Whats your name ? ")
age = input("Whats your age ? ")
#
####  Metodo antigo
# Primeira forma
message1 = "Hello {fname} your age is {fage}".format(fname=name, fage=age)
print(message1)

# Segunda forma
message2 = "Ola {0} sua idade é {1}".format(name, age)
print(message2)

# Terceira forma, o python assume ordem das variáveis
message3 = "Ola {} voce está velho já tem {} ".format(name, age)
print(message3)

#### metodo atual
# vamos declarar year como inteiro, note que a função f converte o inteiro para string
year = 2022
print(f"Hello {name}, in {year} you had {age} chances to be a better person... ")
