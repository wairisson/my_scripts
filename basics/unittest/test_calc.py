# importa biblioteca unittest
import unittest
import calc

class TestCalc(unittest.TestCase):

# a função deve ter seu nome iniciado com "test"
    def test_add(self):
        result = calc.add(10, 5)
        self.assertEqual(result, 15)
        self.assertEqual(calc.add(10, 5), 15) # Forma mais prática de realizar o teste da linha anterior
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)       
# note que estrutura do assert é self.assertEqual(o que deve ser testado, resultado esperado)

#### Executando o código
# Ao executar da forma abaixo nada acontece
#  python test_calc.py 
#
####  Para executar o código corretamente usar o comando abaixo
#  python -m unittest test_calc.py 
#....  # estes pontos indicam sucesso
#----------------------------------------------------------------------
#Ran 4 test in 0.000s
#
#OK
# Embora tenhamos multiplos testes dentro de cada função como eles estão contidos todos em 
# apenas 4 funções então contam como apenas 4 testes


# A função abaixo deve retornar falha de propósito
#    def test_add_fail(self):
#        result = calc.add(10, 5)
#        self.assertEqual(result, 13)

"""
## SAIDA
 FAILED (failures=1)
(.venv) [devasc@labvm unittest](main)$ python -m unittest test_calc.py 
.F # Aqui temos um ponto (sucess) e um F (fail)
======================================================================
FAIL: test_add_fail (test_calc.TestCalc)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/devasc/labs/my_scripts/basics/unittest/test_calc.py", line 28, in test_add_fail
    self.assertEqual(result, 13)
AssertionError: 15 != 13  # aqui o resultado do test indica qual o erro

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=1) """
