numeros = []

while len(numeros) < 7:
    print("Escribe 7 numeros")
    numeros = int(input())
    numeros.append(numeros)
    if len(numeros) == 7:
        ultimo = numeros.pop()
        numeros.insert(0, ultimo)

    print("La Lista rotada quedaria asi:")

    print(numeros)


