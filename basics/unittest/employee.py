
import requests


class Employee:
    """A sample Employee class"""
# Variável constante usada para cálculo de aumento de 5%
    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

# Função retorna email composto pelo  firstname.lastname
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

# Função retorna nome completo  composto pelo  firstname lastname
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

# Função retorna valor do salário do funcionário com aumento de 5%
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def monthly_schedule(self, month):
        response = requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'