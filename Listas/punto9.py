#Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# Mostrar el total vendido por cada producto.
# Mostrar el día con mayores ventas totales.
# Indicar cuál fue el producto más vendido en la semana

ventas = [] 
for i in range(4):
    producto = []
    print(f"Introduce las ventas del Producto {i+1}")
    for j in range (7):
        ventas_dia = int(input(f"Día {j+1}: "))
        producto.append(ventas_dia)
    ventas.append(producto)
    total_producto = sum(producto)
    print(f"El total vendido del Producto {i+1} es de {total_producto}")    

total_dias = [0] * 7
for j in range(7):
    for i in range(4):
        total_dias[j] += ventas[i][j]   
mayor_dia = max(total_dias)
dia_mayor = total_dias.index(mayor_dia) + 1
print(f"El día con mayores ventas totales fue el Día {dia_mayor} con un total de {mayor_dia}")

total_productos = [0] * 4
for i in range(4):
    total_productos[i] = sum(ventas[i])
mayor_producto = max(total_productos)
producto_mas_vendido = total_productos.index(mayor_producto) + 1
print(f"El producto más vendido en la semana fue el Producto {producto_mas_vendido} con un total de {mayor_producto}")
print(ventas)


