"""
 Saindo de loops com break

 Funciona igual nas linguagens java ou C
"""

# Exemplo 1
for numero in range(1, 11):
    if numero >= 7:
        break
    else:
        print(numero)

print("saiu do loop")

# Exemplo 2
while True:
    comando = input("digite 'sair' para sair: ")
    if comando == "sair":
        break
