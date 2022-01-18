"""
Ranges

- Precisamos conhecer o loop for para usar os ranges.
- Precisamos conhecer o range para utilizar melhor o loop for.

Range são utilizados para gerar sequencias numericas, não de forma aleatoria,
mais sim de maneira de especificada.

Formas gerais:

# Forma 1

range(valor_de_parada)

OBS: o valor_de_parada nao inclusive (inicio padrao 0, e passo de 1 em 1

# Exemplo da forma 1
for num in range(11) # Ultimo numero nunca e colocado somente seu anterior
    print(num) # 1,2,3,4,5,6,7,8,9,10

# Forma 2

range(valor_inicial, valor_de_parada)

# Exemplo da forma 2
for num in range(1,11) # Se o valor inial não for especificado sera igual a 0
    print(num) # 1,2,3,4,5,6,7,8,9,10

# Forma 3

range(valor,inicial valor_de_parada, passo)

# Exemplo forma 3
for num in range(1, 11, 2) # Sera passado a quantidade de numeros especificados.
    print(num) # 1,3,5,7,9

# Forma 4

range(valor_inial, valor_final, valor_reverso)

# Exemplo forma 4
for num in range(10, -1, -1) # O valor sera reverso caso colocado numeros negativos no passo
    print(num) # 10,9,8,7,6,5,4,3,2,1
"""
