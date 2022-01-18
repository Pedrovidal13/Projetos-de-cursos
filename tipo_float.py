"""
Tipo float

Tipo real, decimal

Casas decimais

OBS: O separador das casas decimais na programação e ponto não virgula.
"""

# Errado do ponto de vista do float, mais gera uma tupla
valor = 1, 23
print(valor)
print(type(valor))


# Certo
valor = 1.02
print(valor)
print(type(valor))


# E possivel fazer dupla atribuicao
valor1, valor2 = 1, 20

print(valor1)
print(type(valor1))

print(valor2)
print(type(valor2))

# Podemos converter um float em um int

"""
OBS: Ao converter o valor float para int perdemos precisao
"""

resultado = 1.20
print(int(resultado))

# Podemos trabalhar com numeros complexos
numero_complexo = 5j
print(type(numero_complexo))