lista = []

while len(lista) < 5:


    print("Escribe 5 Productos que quieras agregar en la lista")
    producto = input()
    lista.append(producto)

if len(lista) == 5:
    print("Ya pusiste tus 5 productos")

    print("Desesas actualizar la lista o eliminar algun producto?")
    print("1= Actualizar")
    print("2= Eliminar")
    print("3= Ver Lista completa")


    opcion = int(input())
    if opcion == 1:
        print("Cual producto desea actulizar?")
        nuevo_producto = input()
        print("Por cual queres cambiarlo?")
        producto_cambio = input()
        indice = lista.index(producto_cambio)
        lista[indice] = nuevo_producto
    elif opcion == 2: 
        print("Cual producto queres eliminar?")
        producto_eliminar = input()
        lista.remove(producto_eliminar)
    elif opcion == 3:
        lista_o = sorted(lista)
        print("Tu lista de productos es:")
        print(lista_o)
    else:
        print("Opcion Incorecta")