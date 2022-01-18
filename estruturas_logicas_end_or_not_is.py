"""
Estruturas logicas: end (e), or (ou), not (not), is (é)

Operadores unarios:
    - not
Operadores binarios:
    - end, or, is

Regras de funcionamento:

Para o "and" e preciso que ambos os valores estejam True
Para o "or" e preciso que somente 1 valor esteja True
Para o "not" o  valor do booleano e invertido, ou seja, se for True é False, se for False é True
"""

ativo = False
logado = True

# Versão com "end"

if ativo and logado:
    print("Bem vindo ao sistema usuario!")
else:
    print("seu e-mail nao foi ativado, ative para poder entrar no sistema")

# Versão com "or"

if ativo or logado:
    print("Bem vindo ao sistema usuario!")
else:
    print("seu e-mail nao foi ativado, ative para poder entrar no sistema")

# Versão com "not"
# Se não estiver ativo, faça isso
if not ativo:
    print("seu e-mail nao foi ativado, ative para poder entrar no sistema")
else:
    print("Bem vindo ao sistema usuario!")

# Versão com "is"

if logado is ativo:
    print("Bem vindo ao sistema usuario!")
else:
    print("seu e-mail nao foi ativado, ative para poder entrar no sistema")

# Ativo é falso?
print(ativo is False)