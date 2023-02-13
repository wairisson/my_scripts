# Scopes
# Local
# Enclosing
# Global
# Built in

# Variável com escopo global
name = "Global Name"

def print_name():
    # Variável com escopo local a função
    name = "Local Name"
    print(name)


def print_name2():
    # De dentro da função é possível acessar uma variável com escopo global, de fora da função não é 
    # possível acessar uma variável que tenha sido definida dentro da funcão ou seja, com escopo local
    print(name)


print(name)
print_name()
print_name2()

def outer_f():
    name01 = "Outerfunction"
    def inner_f():
        name01 = "Inerfunction"
    inner_f()
    return name01


print(outer_f())

