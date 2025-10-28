#Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

usuario_peso = float(input("Ingresa tu peso en kiogramos:"))

usuario_altura = float(input("Ingresa tu altura en metros:"))

icm_resultado = calcular_imc(usuario_peso, usuario_altura)

print(f"Tu indice de masa corporal (IMC) es: {icm_resultado}")

