#Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, vive):
    return print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {vive}")

nombre_usuario = input("Por favor, ingresa tu nombre:")
apellido_usuario = input("Ingresa tu aapellido:")
usuario_edad = input("Decime tu edad:")
usuario_vive = input("Donde vivis?")

informacion_personal(nombre_usuario, apellido_usuario, usuario_edad, usuario_vive)

