"""the name of an ordinary variable is the name of its content;
the name of a list is the name of a memory location where the list is stored."""

"""The assignment: list_2 = list_1 copies the name of the array, not its contents. In effect, the two names 
(list_1 and list_2) identify the same location in the computer memory.
 Modifying one of them affects the other, and vice versa."""

list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)

"""
Fortunately, the solution is at your fingertips ‒ it's called a slice.

A slice is an element of Python syntax that allows you to make a brand new copy of a list, or parts of a list.

It actually copies the list's contents, not the list's name.

This is exactly what you need. Take a look at the snippet below:
"""
 
list_1 = [1, 2, 3]
#Copy content from list 1 to list 2
list_2 = list_1[:]
#Change value of index 0 in list 1
list_1[0] = 4

print(list_1)
print(list_2)



"""
A slice of this form makes a new (target) list, taking elements from the source list ‒ the elements of the indices from start to end - 1.
"""

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3] # takes  indices equal to 1 and 2 (but not 3).
print(new_list)

new_list = my_list[1:4] # takes  indices equal to 1, 2 and 3 (but not 4).
print(new_list)


#3.6.3 Slices – negative indices

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)

# Print from start to index 2 but not 3
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list)

# Print from index 3 to the end
my_list = [10, 8, 6, 4, 2]
new_list = my_list[3:]
print(new_list)

# delete from index 1 to 2 but not 3
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)

# delete all list content, but the list still
my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list)

# delete entire list
my_list = [10, 8, 6, 4, 2]
del my_list
print(my_list)

#3.6.4 The in and not in operators
#Python offers two very powerful operators, able to look through the list in order to check whether a specific value is stored inside the list or not
my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)

#3.6.5 Lists – some simple programs
my_list = [7, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(largest)


my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]
 
for i in my_list:
    if i > largest:
        largest = i
 
print(largest)

#find the location of a given element inside a list:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print("Element found at index", i)
else:
    print("absent")


my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Write your code here.
my_new_list = []
for i in my_list:
    print(i)
#
print("The list with unique elements only:")
print(my_list)





