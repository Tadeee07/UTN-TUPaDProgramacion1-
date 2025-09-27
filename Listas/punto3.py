lista_par = []
lista_impar = []
contador = 0

while contador < 15:
    print("Escribe 15 numeros del 1 al 100")

    numero =int(input())

    if numero % 2 == 0 and 1 <= numero <= 100:
        lista_par.append(numero)
    else:
        lista_impar.append(numero)
    
    contador = contador + 1 

print(f"Los numeros pares son {lista_par}")
print(f"Los numeros impares son {lista_impar}")

