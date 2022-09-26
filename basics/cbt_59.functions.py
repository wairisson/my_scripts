def adder(a, b):
    print(a+b)

#Com numeros executa a operação
adder(9, 9)
#Com string concatena
adder("Wairisson", "Gomes")

def gen_email(username, provider):
    """
    This is an example of docstring
    This function takes 2 arguments, username and provider (eg google, outlook) 
    and the concatenates it creating a valid e-mail address
    """
    print(f"Your e-mail is {username}@{provider}.com")

gen_email("wairisson", "hotmail")

#para visualizar o docstring basta usar o comando help passando a função como parâmetro
help(gen_email)
#outra forma de visualizar é usando método __doc__
# ele exibe de forma não paginada o conteúdo do docstring
print(gen_email.__doc__)

