# Estrutura do range
# from range (1, 10) onde 1 é inclusivo, ou seja conta-se, e 10 é exclusivo ou seja não se conta
# Na prática o contador será de 1 a 9
for x in range(0,10):
    print(f"interface g0/{x}")
# Saída
#interface g0/0
#interface g0/1
#interface g0/2
#interface g0/3
#interface g0/4
#interface g0/5
#interface g0/6
#interface g0/7
#interface g0/8
#interface g0/9
print("\n","================","\n")
# Imprime de 0 a 10 de 2 em 2
for x in range(0,10,2):
    print(f"interface g0/{x}")

for x in range(1,256):
    print(f"ping 192.168.0.{x}")