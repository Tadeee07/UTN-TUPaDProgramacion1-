


#1) 
precios_frutas = {"Banana": 1200, "Anana":2500, "Melon": 3000, "Uva": 1450}
precios_frutas = {"Naranja": 1200, "Manzana": 1500, "Pera": 2300}
print(precios_frutas)

#2)
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melon"] = 2800
print(precios_frutas)

#3)
frutas = list(precios_frutas.keys())
print(frutas)


#4)
agenda_telefonica = {}
for i in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número telefónico: ")
    agenda_telefonica[nombre] = numero
consulta = input("Ingrese el nombre del contacto a consultar: ")
if consulta in agenda_telefonica:
    print(f"El número de {consulta} es {agenda_telefonica[consulta]}")
else:
    print(f"No se encontró el contacto {consulta}")

#5)
frase = input("Ingrese una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)
contador_palabras = {}
for palabra in palabras:
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1
print("Cantidad de veces que aparece cada palabra:", contador_palabras)

#6)
alumnos = {}
for i in range(3):
    nombre = input("Ingrese el nombre del alumno: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Ingrese la nota {j+1} de {nombre}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {nombre} es {promedio}")

#7)
parcial1 = {101, 102, 103, 104}
parcial2 = {103, 104, 105, 106}
aprobados_ambos = parcial1.intersection(parcial2)
print("Estudiantes que aprobaron ambos parciales:", aprobados_ambos)
aprobados_solo_uno = parcial1.symmetric_difference(parcial2)
print("Estudiantes que aprobaron solo uno de los dos parciales:", aprobados_solo_uno)
aprobados_al_menos_uno = parcial1.union(parcial2)
print("Estudiantes que aprobaron al menos un parcial:", aprobados_al_menos_uno)

#8)
stock_productos = {}
while True:
    accion = input("Ingrese 'consultar', 'agregar' o 'nuevo' (o 'salir' para terminar): ")
    if accion == 'salir':
        break
    producto = input("Ingrese el nombre del producto: ")
    if accion == 'consultar':
        if producto in stock_productos:
            print(f"El stock de {producto} es {stock_productos[producto]}")
        else:
            print(f"{producto} no existe en el stock.")
    elif accion == 'agregar':
        if producto in stock_productos:
            cantidad = int(input("Ingrese la cantidad a agregar: "))
            stock_productos[producto] += cantidad
            print(f"Nuevo stock de {producto} es {stock_productos[producto]}")
        else:
            print(f"{producto} no existe en el stock.")
    elif accion == 'nuevo':
        cantidad = int(input("Ingrese la cantidad inicial: "))
        stock_productos[producto] = cantidad
        print(f"{producto} agregado con un stock de {cantidad}")

#9)
agenda_eventos = {}
while True:
    dia = input("Ingrese el día (o 'salir' para terminar): ")
    if dia == 'salir':
        break
    hora = input("Ingrese la hora: ")
    evento = input("Ingrese el evento: ")
    agenda_eventos[(dia, hora)] = evento
consulta_dia = input("Ingrese el día a consultar: ")
consulta_hora = input("Ingrese la hora a consultar: ")
if (consulta_dia, consulta_hora) in agenda_eventos:
    print(f"El evento en {consulta_dia} a las {consulta_hora} es: {agenda_eventos[(consulta_dia, consulta_hora)]}")
else:
    print("No hay eventos programados en esa fecha y hora.")


#10)
paises_capitales = {'Argentina': 'Buenos Aires', 'Brasil': 'Brasilia', 'Chile': 'Santiago'}
capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}
print("Diccionario invertido de capitales y países:", capitales_paises)



