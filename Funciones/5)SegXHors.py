#Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

usuario_segundos = int(input("Por favor, ingresa la cantidad de segundos:"))
horas_convetidas = segundos_a_horas(usuario_segundos)
print(f"La cantidad de {usuario_segundos} segundos en horas es: {horas_convetidas}")

