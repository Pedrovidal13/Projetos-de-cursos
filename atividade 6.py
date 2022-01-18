palavra = str(input("invertebrado ou vertebrado?: "))
palavra2 = str(input("ave ou mamifero?: "))
palavra3 = str(input("onivoro ou erbivoro?: "))

if palavra == "vertebrado":
    if palavra2 == "ave":
        if palavra3 == "carnivoro":
            print("aguia")
        else:
            print("pombo")
    else:
        if palavra3 == "onivoro":
            print("humano")
        else:
            print("vaca")
else:
    print("incompleto")
