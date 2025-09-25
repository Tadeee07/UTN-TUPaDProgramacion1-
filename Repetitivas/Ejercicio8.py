cont_n = 0
cont_p = 0
cont_pa = 0
cont_im = 0
contador = 0

while contador <= 100:
    print("Escribe un numero")

    num = int(input())

    if num > 0:
        cont_p = cont_p + 1
    else:
        cont_n = cont_n + 1
    
    if num % 2 == 0:
        cont_pa = cont_pa + 1
    else:
        cont_im = cont_im + 1

    contador = contador + 1 



print(f"NUMERO DE PARES {cont_pa}")
print(f"NUMERO DE IMPARES {cont_im}")
print(f"NUMERO DE POSITIVOS {cont_p}")
print(f"NUMERO DE NEGATIVOS {cont_n}")