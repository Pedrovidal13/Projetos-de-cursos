"""
Escopo de variaveis

Dois casos de escopo:

1 - Variavel globais;
    - Variavel globais são reconhecidas, ou seja, seu escopo compeende, todo o o programa

2 - Variavel locais;
    - Variaveis locais são  reconhecidas apenas no bloco onde foram declaradas, ou  seja, seu escopo
    esta limitado ao bloco onde foi criada.

Para declarar variaves em Python fazemos:

nome_da_variavel = valor_da_variavel

Python e uma linguagem de tipagem dinamica. Isso significa que
a o declarar uma varial, nos nao colocamos o tipo de dado dela.
Esse tipo e inferivel ao contribuirmos o valor da mesma.

Exemplo em C:
int numero = 42;

Exemplo em java:
int numero = 42;

"""

numero = 42  # Exemplo de variavel global
print(numero, type(numero))

numero = "pedro"
print(numero, type(numero))

nao_existe = "oi"
print(nao_existe)

numero = 42
# novo = 0

if numero > 10:
    novo = numero = 10  # A varialvel "novo" esta declarada localmente dentro do bloco do if. por tanto e local
    print(novo, type(novo))

print(novo)
