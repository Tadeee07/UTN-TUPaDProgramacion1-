#Crear una lista con los nombres de 8 estudiantes presentes en clase.
#Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
#Mostrar la lista final actualizada

estudiantes = []

print("Sos un profesor y tenes que poner los nombres de tus 8 estudiantes presentes")
while len(estudiantes) < 8:
    print("Nombre del estudiante:")
    nombre = input()
    estudiantes.append(nombre)

if len(estudiantes) == 8:
    print("Tu lista esta completa")

    print("Que deseas hacer?")
    print("1= Agregar un estudiante")
    print("2= Eliminar un estudiante")
    print("3= Ver Lista completa")

    opcion = int(input())
    if opcion == 1:
        print("A quien desas agrear?")
        nuevo_estudiante = input()
        estudiantes.append(nuevo_estudiante)
        print("Agregado!!")
    elif opcion == 2:
        print("Cual estudiante queres eliminar?")
        estudiante_eliminar = input()
        estudiantes.remove(estudiante_eliminar)
        print("Eliminado!!")
    elif opcion == 3: 
        estudiantes_o = sorted(estudiantes)
        print("Tus alumnos precentes son:")
        print(estudiantes_o)
    else:
        print("Opcion Incorecta")

else:
    print("Error, no se completo la lista") 
    

