# As funções min e max permitem selecionar os valores mínimo e máximo detre um conjunto de variáveis
list_of_numbers  = [2, 5, 10, 500, 13, 4, 67, 33]
print(f"A quantidade de items da lista é {len(list_of_numbers)}")
print(f"O menor valor dentre os items da lista é {min(list_of_numbers)}")
print(f"O maior valor dentre os items da lista é {max(list_of_numbers)}")

list_of_names_1  = ["Nicolas", "Filipe", "Wairisson"]
print(f"O primeiro nome da ordem alfabética é:  {min(list_of_names_1)}")
print(f"O último nome da ordem alfabética é:  {max(list_of_names_1)}","\n")

#No caso abaixo o Wairisson será exibido pois o Python testa primeiro A-Z depois a-z
list_of_names_2  = ["nicolas", "filipe", "Wairisson"]
print(f"O primeiro nome da ordem alfabética é:  {min(list_of_names_2)}")
print(f"O último nome da ordem alfabética é:  {max(list_of_names_2)}")

