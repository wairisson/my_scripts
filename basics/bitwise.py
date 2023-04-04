# Referencia
# https://www.youtube.com/watch?v=cylq8mUW44Q

a = 5
b = bin(a)
# retorna 0b101
print(b)
#remover 0b e retorna apenas 101
print(b[2:])

c = a<<3
print(bin(c))

d = 5
e = 60
# Printando em binário
print(bin(5),bin(2))

print("bar","#"*50, "\n")
# usando | (bar) ‒ bitwise disjunction  (operação or binária)
print(bin(d|e)) # retorno 0b111, retorna 1 se ao menos um dos bits for 1
print("bar","#"*50, "\n")

print("ampersand","#"*50, "\n")
# usando & (ampersand) ‒ bitwise conjunction  (operação and binária)
print(bin(d&e)) # retorno 0b0, retorna 1 apenas se ambos os bits forem 1
print(bin(7&5)) # retorno 0b101, 5 em decimal
print("ampersand","#"*50, "\n")

print("tilde","#"*50, "\n")
# ~ (tilde) ‒ bitwise negation inverte o sinal e subtrai 1
# Ex: ~2 = -3, ~5 = -6, ~10 = -11 
print(f" variável e em decimal vale {e}")
print(f" variável e em binário vale {bin(e)}")
# f recebe negação de e
f = ~e 
print(f" variável f em decimal vale {f}")
print(f" variável f em binário vale {bin(f)}")
print("tilde","#"*50, "\n")

print("CARETˆ","#"*50, "\n")
# ^ (caret) ‒ bitwise exclusive or (xor).
# verdadeiro somente quando exclusivamente apenas 1 valor for verdadeiro
# ex: 
# 0 ^ 0 = 0
# 1 ^ 1 = 0 
# 0 ^ 1 = 1 
# 1 ^ 0 = 1 

a = 2
b = 2
c = a ^ b
d = a ^ 1
print(c) # Retorna 0 pois 10 XOR 10 = 00 
print(d) # Retorna 3 pois 10 XOR 01 = 11 
print("CARETˆ","#"*50, "\n")

flag_register = 0x1234
print(bin(flag_register))

the_mask = 8

if flag_register & the_mask:
    # My bit is set.
    print("My bit is set.")
else:
    # My bit is reset.
    print("My bit is reset.")

print("Binary left shift and binary right shift","#"*50, "\n")
#3.6 Binary left shift and binary right shift
#right shift: remove bits a direita, ex: 10001 >> 1 se torna 1000
#left shift: adiciona bits a direita, ex: 10001 << 2 se torna 1000100

var = 17
var_right = var >> 1
var_left = var << 2
print(bin(var),  bin(var_right), bin(var_left))
print(var, var_right, var_left )
print("Binary left shift and binary right shift","#"*50, "\n")

# Exercicios
x = 4
y = 1
 
a = x & y
b = x | y
c = ~x  # tricky!
d = x ^ 5
e = x >> 2
f = x << 2

print(f"o resultado de {bin(x)} x {bin(y)} é {bin(a)}")
print(f"o resultado de {bin(x)} + {bin(y)} é {bin(b)}")
print(f"o resultado de  negação de {bin(x)}  é {bin(c)}")

print(c)