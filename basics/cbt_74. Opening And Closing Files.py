# Open  é usado para abertura de arquivos
# ATENÇAO : o arquivo deve estar no mesmo diretório do script
# para visualizar atributos e métodos disponíveis abrir ipython e 
# executar dir(open)
# Por default é aberto em modo somente leitura
file = open("cbt_74.txt")
file.close()
print(type(file))
print(file)

# o arquivo deve ser fechado sob pena de modificações feitas não terem efeito até que ele seja fechado.

# CONTEXT MANAGER
#Para um código mais limpo o context manager pode ser usado 
# O CM fecha automáticamente o arquivo
# Exemplo:
with open("cbt_74.txt") as file:
    print(type(file))

# o Context Manager se comporta como uma função identando o código, assim que ele termina sua execução
# o arquivo é fechado automaticamente

print("###################################")
with open("cbt_74.txt", "r") as file_ro:
    # para ler o conteúdo do arquivo o método read deve ser usado
    file_content = file_ro.read()
    # exemplo abaixo lê apenas os 5 primeiros caracteres
#    file_content = file_ro.read(5)

# Verificando tipo
print(type(file_content))
# Exibindo conteúdo 
print(file_content)
# convertendo a string para uma lista composta pelas palavras
print(file_content.split())

print("###################################", "\n")
# Lendo linhas
with open("cbt_74.txt", "r") as file_ro:
    # para ler uma linha somente do arquivo o método readline deve ser usado
    file_content = file_ro.readline()
    print(file_content)

print("###################################", "\n")

with open("cbt_74.txt", "r") as file_ro:
    # O método readlines lê as linhas e as coloca como items dentro de uma lista
    file_content = file_ro.readlines()
    print(file_content)