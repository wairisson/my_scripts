#1.1 Definindo a classe
class operations:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2  = num2

# 2. Adicionando um método soma a para classe
    def sum(self):
        sum_result = self.num1+self.num2
        print(f"the sum of {self.num1} and {self.num2} is {sum_result}.")

# 2. Adicionando um método multiplicação para classe
    def multiply(self):
        multiply_result = self.num1*self.num2
        print(f"the multiply result of {self.num1} times {self.num2} is {multiply_result}.")


