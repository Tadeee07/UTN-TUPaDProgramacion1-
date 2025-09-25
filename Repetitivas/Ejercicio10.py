
print("Ingresá un número:")
num = int(input())
invertido = 0
while num > 0:
    resto = num % 10
    invertido = invertido * 10 + resto
    num //= 10
print(invertido)