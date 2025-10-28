#Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#resultado usando la función.


def celsius_a_fahrenheit(celsius):
    faharemheit = (celsius * 9/5) + 32
    return faharemheit

usuario_celsius = float(input("Ingresa la Tmeperatura en grados Celsius:"))
resultados_fahrenheit = celsius_a_fahrenheit(usuario_celsius)

print(f"La temperatura de {usuario_celsius}°C es igual a {resultados_fahrenheit}°F")

