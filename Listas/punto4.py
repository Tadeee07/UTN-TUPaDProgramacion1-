datos = [1, 3, 5, 3, 7,  1, 9, 5, 3]
sin_repetidos = []

for n in datos:
    if n not in sin_repetidos:
        sin_repetidos.append(n)

print(sin_repetidos)

