list_in_list = ["item1.1","item1.2",["item2.1","item2.2"], "item1.3", "item1.4"]
print(list_in_list)
print(list_in_list[0])
print(list_in_list[1])
print(list_in_list[2])
print(list_in_list[2][0])
print(list_in_list[2][1])
print(list_in_list[3])
print(list_in_list[4])

print("===================", "\n")
#iterando sobre a lista 
for item in list_in_list:
    print(item)
print("===================", "\n")
#iterando sobre a lista dentro da lista
for item in list_in_list[2]:
    print(item)
