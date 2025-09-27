#Crear una matriz con las notas de 5 estudiantes en 3 materias.
#Mostrar el promedio de cada estudiante.
#Mostrar el promedio de cada materia.

notas = []
for i in range(5):
    estudiante = []
    print(f"Introduce las notas del Estudiante {i+1}")
    for j in range (3):
        notas_materias = int(input(f"Materia {j+1}: "))
        estudiante.append(notas_materias)
        notas.append(estudiante)
        promedio_estudiante = sum(estudiante) / len (estudiante)
    print(f"El promedio del Estudiante {i+1} es de {promedio_estudiante}")

    promedio_materia1 = sum(notas[0][0], notas[1][0], notas[2][0], notas[3][0], notas[4][0]) / 5 
    promedio_materia2 = sum(notas[0][0], notas[1][0], notas[2][0], notas[3][0], notas[4][0]) / 5 
    promedio_materia3 = sum(notas[0][0], notas[1][0], notas[2][0], notas[3][0], notas[4][0]) / 5 

    print(f"El promedio de la Materia 1 es de {promedio_materia1}")
    print(f"El promedio de la Materia 2 es de {promedio_materia2}")
    print(f"El promedio de la Materia 3 es de {promedio_materia3}")