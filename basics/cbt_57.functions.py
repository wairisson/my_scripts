# funcões são pedaços de código
# sempre possuem um return que por default é none
# Funcões embutidas do pytho podem  ser encontradas no link abaixo:
# https://docs.python.org/3/library/functions.html
#
#Usando  funções embutidas
# A função help é similar ao man do linux


help(print)

# isinstance pode ser usado para verificar se uma variável e um tipo determinado de dado

#Testa se number == int (false)
number = "5"
result = isinstance(number, int)
print(result)

result = isinstance(number, tuple)
print(result)

result = isinstance(number, dict)
print(result)

result = isinstance(number, set)
print(result)


#Testa se new_number == int (true)
new_number = 5
result = isinstance(new_number, int)
print(result)

my_list = [1, 2, 3, 4, [5,55,555], 6, 7, 8]
for num in my_list:
    if isinstance(num,list):
        for n in num:
            if n == 5:
                print("The number 5 is present in child list")
    else:
        if num == 5:
            print("The number 5 is present in main list")

print(len(my_list))