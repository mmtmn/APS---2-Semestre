def main():
    bairro = str(input("Em qual bairro você esta? "))
    material = str(input("Qual material você gostaria de reciclar? "))
    quantidade = int(input("Qual a quantidade que você gostaria de reciclar? (em quilos) "))

    print("Você esta no", bairro)
    print("Você quer doar", material)
    print("E a quantidade, em quilos, é:", quantidade)

main()

def localização(): 
    locais = ["local1", "local2", "local3", "local4"]
    cordenada = int(input("Qual a sua cordenada?"))
    if cordenada == 1:
        print(locais[0])
    elif cordenada == 2:
        print(locais[1])
    elif cordenada == 3:
        print(locais[2])
    elif cordenada == 4:
        print(locais[3])
    else:
        print("error")

localização()