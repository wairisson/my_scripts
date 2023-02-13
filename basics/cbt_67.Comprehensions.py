# Comprehensions
# List, Dicts and sets
#
interface_list  = ["g0/0","f0/1","f0/2","g0/3","g0/4", "lo0"]
gig_list = []

for int in interface_list:
    if int.startswith("g"):
        gig_list.append(int)

print(gig_list)

# now using comprehension
# first "i" is the expression, it receive the result of iteration
# "for i in interface_list" this is the iteration
# last part "if i.startswith("g")" is the conditional
gig_list2 = [i for i in interface_list if i.startswith("g")]
print(gig_list2)

# no exemplo abaixo o resultado da iteração é passado para função
# que altera as letras para maiúsculas e depois armazena na lista
gig_list3 = [i.upper() for i in interface_list if i.startswith("g")]
print(gig_list3)

#Dictionaty comprehension
#Codigo escrito sem comprehension
age = {"Wairisson":38, "Tayná":30, "Mick":4,"Mel":3, "Nick":1}
dict01 = {}
for k,v in age.items():
    if v > 18:
        dict01[k] = v

print(dict01)

#Codigo escrito com comprehension
dict02 = {k:v for k,v in age.items() if v > 18}
print(dict02)