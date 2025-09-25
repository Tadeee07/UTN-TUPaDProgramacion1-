contador = 0

print("Escribe valores enteros y si quieres terminar el programa escribe 0")
num = int(input())


while num != 0:

    contador = contador + num
    print("Escribe valores enteros y si quieres terminar el programa escribe 0")
    num = int(input())
    if num == 0:
        break

print(f"La suma de los enteros es {contador}" )