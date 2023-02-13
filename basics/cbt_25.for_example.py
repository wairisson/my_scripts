#
## IF ##1
#
age = input("Informe sua idade ")

if int(age) > 21:
    print("ok get your a beer")
elif int(age) >= 17:
    print("You are too young to drink, but you can vote")
else:
    print("You are too young to drink, get out here!")
#
# IF #2
#
vendor = input("Informe o vendor \n Opções:\n -- cisco\n -- huawei \n ")

if vendor == "cisco":
    print("show ip int br")
elif vendor == "huawei":
    print("display ip int br")
else:
    print("Vendor desconhecido.")

