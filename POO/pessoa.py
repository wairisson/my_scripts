# a classe é como se fosse o molde ou template
class Pessoa:
    def __init__ (self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
#criação do método comer (similar a uma funcão normal)
    def comer(self, alimento):
        if self.comendo:
            print(f"{self.nome} já está comendo.")
            return

        print(f"{self.nome} está comendo {alimento}")
        self.comendo =  True

    def parar_comer(self):
        if not self.comendo:
            print(f"{self.nome} não está comendo.")
            return
        
        print(f"{self.nome} parou de comer.")
        self.comendo = False

    