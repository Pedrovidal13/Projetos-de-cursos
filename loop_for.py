"""
Estrutura de repetição:
    loop -> estrutura de repetição
    for -> uma dessas estruturas

C ou java

for(int i = 0; i < 10; i++){
    //execução do loop
}

Python

for i in interavel:
    //execução do loop

Utilizamos loops para iterar sobre sequencias ou sobre valores iteraveis

Exemplo de iteraveis
String, Lista, range
Str:
str = 'ola tuod bem?',

Lista = [1, 2,3,4,5,6]

Range:
numero = range(0,100)


str1 = "Pedro"

lista = [1, 2, 23, 20, 10, 4, 8]

numero = range(0, 100) # Temos que transformar em uma lista

# Exemplo de for 1
for letra in str1:
    print(letra)

# Exemplo de for 2
for numero in lista:
    print(numero)


# Exemplo de for 3
for numero in range(0,100,3):  # Range(valor_inicial,valor_final,valor_multiplicado) OBS: o numero final nao e incluido
    print(numero)


Enumerate :

(0, P), (1, E) (2, D), (3, R), (4, O)

for indice, letra in enumerate(nome):
    print(nome[indice])

for indice, letra in enumerate(nome):
    print(letra)
    
for _, letra in enumerate(nome):
    print(letra)

OBS: Quando nao precisamos de um valor, podemos descarta-lo utilizando underline (_)

nome = "Pedro"
lista = [1,2,3,4,5,6]
numero = range(0, 10) # Temos que transformar em uma lista!

for valor in enumerate(nome):
    print(valor)

quantidade = int(input("Quantas vezes esse loop deve rodar?: "))
soma = 0

for n in range(1, quantidade + 1):
    num = int(input(f"Rodada {n} Digite {quantidade} numeros para fazer a soma"))
    soma = soma + num
    quantidade -= 1
print(f"a soma dos numeros e {soma}")
"""
nome = "pedro"
for i in nome:
    print(i, end="")
