contador = 1
prom = 1
acumulador = 0
num = 0

while contador <= 100:
    print("Introduce un numero")

    num = int(input())

    acumulador = acumulador + num

    prom = acumulador / contador

    contador = contador + 1

print (f"El Promedio de todos los numero introducidos es {prom}")