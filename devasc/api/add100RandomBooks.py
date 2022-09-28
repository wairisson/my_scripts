import requests
import json
from faker import Faker

#A biblioteca faker disponibiliza vários métodos para geração de dados para testes e exercícios
#Exemplos:
var_fake = Faker()
print(var_fake.name())
print(var_fake.isbn13())
print(var_fake.catch_phrase())

for i in range(10):
    print(var_fake.name())
    