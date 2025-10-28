#Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a,b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    divicion = a / b
    return (suma, resta, multiplicacion, divicion)

num1 = float(input("Ingresa el primer numero:"))

num2 = float(input("Ingresa el segundo numero:"))

resultados = operaciones_basicas(num1, num2)

print(f"La suma de {num1} y {num2} es {resultados[0]}")
print(f"La resta de {num1} y {num2} es {resultados[1]}")
print(f"La multiplicacion de {num1} y {num2} es {resultados[2]}")
print(f"La divicion de {num1} y {num2} es {resultados[3]}")


