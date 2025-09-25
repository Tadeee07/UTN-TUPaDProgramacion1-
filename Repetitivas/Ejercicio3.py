contador = 0
print("Escribe 2 valores enteros")
num1 = int(input())

print("Numero 2")

num2 = int(input())

for i in range(num1 + 1, num2):
    contador += i

print(contador)