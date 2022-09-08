# 1 Definindo e instanciando a classe
#1.1 Definindo a classe
class Location:
    def __init__(self, name, country):
        self.name = name
        self.country  = country

# 2. Adicionando um método a para classe
    def myLocation(self):
        print(f"Hi, my name is{self.name} and I live in {self.country}.")


# 1.2 Instanciando a classe
loc = Location("Wairisson", "Brasil")
print(loc.name)
print(loc.country)
print(type(loc))
print(type(loc.name))
print(type(loc.country))

# 2.1 Instanciar classe múltiplas vezes e chamar método myLocation
loc1 = Location("Wairisson", "Maraba")
loc2 = Location("Wairisson", "Brasilia")
loc3 = Location("Wairisson", "São Paulo")
loc1.myLocation()
loc2.myLocation()
loc3.myLocation()



