
# Actividad 1: Crear archivo inicial con productos
with open("productos.txt", "w") as file:
    file.write("Lapicera,120.5,30\n")
    file.write("Cuaderno,250.0,15\n")
    file.write("Mochila,1500.0,10\n")

# Actividades 2 a 6: Leer, mostrar, agregar, buscar y guardar productos
def cargar_productos():
    productos = []
    with open("productos.txt", "r") as file:
        for linea in file:
            nombre, precio, cantidad = linea.strip().split(",")
            productos.append({
                "nombre": nombre,
                "precio": float(precio),
                "cantidad": int(cantidad)
            })
    return productos
def mostrar_productos(productos):
    for producto in productos:
        print(f"Producto: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")
def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    with open("productos.txt", "a") as file:
        file.write(f"{nombre},{precio},{cantidad}\n")
def buscar_producto(productos):
    nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
    for producto in productos:
        if producto["nombre"].lower() == nombre_buscar.lower():
            print(f"Producto encontrado: {producto}")
            return
    print("Producto no encontrado.")
def guardar_productos(productos):
    with open("productos.txt", "w") as file:
        for producto in productos:
            file.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
# Cargar productos desde el archivo
productos = cargar_productos()
# Mostrar productos
mostrar_productos(productos)
# Agregar un nuevo producto
agregar_producto()
# Recargar productos para incluir el nuevo
productos = cargar_productos()
# Buscar un producto por nombre
buscar_producto(productos)
# Guardar los productos actualizados en el archivo
guardar_productos(productos)




