import random
num_random = random.randint(1,10)
print("Escribe un numero cualquiera del 1 al 9")
num = int(input())

while num != num_random: 
    num_random = random.randint(1,10)
    print("Escribe un numero cualquiera del 1 al 9")
    num = int(input())
    if num == num_random: 
        break

print( f"ADIVINASTE EL NUMERO ES {num}")