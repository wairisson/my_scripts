# Meta caracteres: . ^ $ * + ? { } [ ] \ | ( )
# | OU
# . Qualquer caractere (com exceção da quebra de linha)
# [] conjunto de caracteres

from itertools import count
import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.
Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''
# usando o | 
#print(re.findall(r'João|Maria', texto))
#print(re.findall(r'João|joão|Maria', texto))
print(re.findall(r'[Jj]oão|[Mm]aria', texto))
print(re.findall(r'[A-Za-z]oão|[A-Za-z]aria', texto))
# buscando números
print(re.findall(r'[0-9]+', texto))
#retorno do comando acima é uma lista, note que noão com j minúsculo não retorna na consulta
print(type(re.findall(r'João|Maria', texto)))
# criando uma lista com o resultado
list_re = re.findall(r'João|Maria', texto)
print(list_re)
# Usando .
print(re.findall(r'João|Maria|ad..tos', texto))

# Usando a flag ignore para ignora o case sensitive
print("===================================================")
print(re.findall(r'jOãO|mARia', texto, flags=re.IGNORECASE))
print(re.findall(r'jOãO|mARia', texto, flags=re.I))

## Exemplo em networking

showver = '''Cisco IOS Software, C2900 Software (C2900-UNIVERSALK9-M), Version 15.4(2)T, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2014 by Cisco Systems, Inc.
Compiled Wed 26-Mar-14 14:14 by prod_rel_team

ROM: System Bootstrap, Version 15.0(1r)M9, RELEASE SOFTWARE (fc1)

pa-blm-rgf-cucme01 uptime is 2 days, 1 hour, 6 minutes
System returned to ROM by power-on
System image file is "flash0:c2900-universalk9-mz.SPA.154-2.T.bin"
Last reload type: Normal Reload
Last reload reason: power-on'''

#print(re.findall(r'Version', showver))