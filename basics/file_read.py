with open('file_a.txt') as f:
    lines = f.read().splitlines()
print ("Exibindo a lista ", lines)
print ("O tipo de dado é: ", type(lines))
#
print ("Posição 0 ", lines[0])
print ("Posição 1 ", lines[1])
print ("Posição 2 ", lines[2])
print ("Posição 3 ", lines[3])