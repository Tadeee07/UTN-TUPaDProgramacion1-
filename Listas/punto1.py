contador = 0
promedio = 0
not_menor = 10
not_mayor = 0


notas = []

while contador < 10:
    print("Escribe la nota de 10 estudiantes")
    nota = int(input())
    notas.append(nota)
    contador = contador + 1 
    
    if nota > not_mayor:
        not_mayor = nota
    elif nota < not_menor:
        not_menor = nota

for nota in notas:
    print(f"las notas son {nota}")

promedio = sum(notas) / len(notas)

print(f"El Promedio de las notas es {promedio}")

print(f"la nota menor en esta lista es {not_menor}")
print(f"la nota mayor en esta lista es {not_mayor}")