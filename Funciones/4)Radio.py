#Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva
#el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva 
#el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

def calcular_area_circulo(radio):
    area = 3.14*(radio**2)
    return area
def calcular_perimetro_circulos(radio):
    perimetro = 2*3.14*radio
    return perimetro

usuario_radio = float(input("Por favor, ingresa el radio del circulo:"))

area_circulo = calcular_area_circulo(usuario_radio)
perimetro_circulo = calcular_perimetro_circulos(usuario_radio)
print(f"El area del circulo es: {area_circulo}")
print(f"El perimetro del circulo es: {perimetro_circulo}")

