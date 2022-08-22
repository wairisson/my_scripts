var0 = 0
var1 = 1
var2 = "2"
var3 = 2.5
var4 = ["1","2", 3, 4.5]
var5 = []
var6 = ["", ""]
var7 = ""
var8 = {"hostname":"R1", "ipv4":"192.168.0.1"}
var9 = {"":""}
var10 = {}
var11 = ("A",var2, 1, 2.3, True)
var12 = ()
var13 = 0.0
var14 = {1,2,3,4}
var15 = set()


list_of_vars = [var0, var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, var11, var12, var13, var14, var15]
count = 0
for var in list_of_vars:
    print(f"conteúdo da var{count}:", var)
    print("O tipo é: ", type(var))
    print("O teste função bool retornou: ", bool(var))
    if var:
        print("O teste IF retornou: Verdadeiro","\n")
    else:
        print("O teste IF retornou: Falso","\n")
    count += 1

