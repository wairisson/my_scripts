my_list = [10, 1, 8, 3, 5]
length = my_list[length]
for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]
 
print(my_list)