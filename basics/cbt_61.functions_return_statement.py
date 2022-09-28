# Neste exemplo a função printa o conteúdo da variável my_e-mail de forma direta quando 
# a função é invocada, porém nota-se que quando se deseja atribuir o resultado da função
#  a variável email que está fora da função a variável recebe "None" que é o retorno default
# de uma função
def generate_email_1(username, provider="gmail"):
    my_email = username+"@"+provider+".com"
    print(my_email)

email = generate_email_1("wairisson")
print(email)


# Neste exemplo como não há um print explicito na função não há nenhuma visualização, o codigo
# é executado dentro da função mas como ela não printa nada na sua execução e nem retorna nenhum
# valor nada será printado na tela
def generate_email_2(username, provider="gmail"):
    my_email = username+"@"+provider+".com"

email = generate_email_2("tayna")
print(email)

# Neste exemplo programamos a função para retornar o conteúdo da variável my_email
# assim agora é possível retornar o resultado do processamento da função para fora da função
# neste exemplo o resultado da função foi armazenado na variável email
def generate_email_3(username, provider="gmail"):
    my_email = username+"@"+provider+".com"
    return my_email

email = generate_email_3("caio")
print(email)

# o print abaixo retornará erro pois a variável my_email somente existe dentro do ambiente da função
#print(my_email)
#NameError: name 'my_email' is not defined

# examplo usando a função generate_email_3
name_list = ["wairisson", "caio", "filipe", "nicolas"]
email_list = []

# itera sobre a lista name_list e adiciona e-mails já gerados noutra lista email_list
for name in name_list:
    email_temp = generate_email_3(name, "cbtnuggets")
    email_list.append(email_temp)

print(email_list)



