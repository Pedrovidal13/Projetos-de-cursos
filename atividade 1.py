"""
"exercicio 3"
#ENTRADA
nome = str(input("nome:"))
salario = int(input("salario:"))
comissao = int(input("quanto voce vendeu?"))

#PROCESSO
salario_Total = salario + comissao * 15 / 100 #ou 0.15

#SAIDA
print(nome, salario_Total)



#exercicio 4

kilometro = int(input("quantos kilometros voce percorreu?:"))
quantos_litros_de_gasolina = int(input("quanto litros de gasolina voce tem?:"))

gasto = quantos_litros_de_gasolina / kilometro

print(gasto)


tempo_gasto = int(input("quanto tempo gastou?"))
velocidade_carro = int(input("a quanto km voce foi?:"))

distancia_total = tempo_gasto * velocidade_carro
litros_precisos = distancia_total / 12

print(distancia_total)
print(litros_precisos)
"""