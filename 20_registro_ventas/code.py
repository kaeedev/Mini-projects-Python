ventas_diarias = {}

while True:
    opcion = input('1. Registrar venta 2.Actualizar cantidad vendida. 3.Calcular total de ventas 4.Salir. Elige una opcion: ')

    if opcion == '1': #registramos las ventas y las añadimos en el diccionario
        producto = input('Ingrese el nombre del producto: ')
        cantidad = int(input('Ingrese la cantidad vendida: '))
        if producto in ventas_diarias:  #si el producto ya esta registrado sumamos la cantidad vendida a las cantidades anteriores
            ventas_diarias[producto] += cantidad
        else:
            ventas_diarias[producto] = cantidad #si no esta registrado añadimos la cantidad vendida
    elif opcion == '2': #actualizar las ventas
        producto = input('Ingrese el nombre del producto a actualizar: ')
        if producto in ventas_diarias:
            nueva_cantidad = int(input('Ingrese la nueva cantidad vendida: '))
            ventas_diarias[producto] = nueva_cantidad
        else:
            print('El producto no existe en las ventas diarias')
    elif opcion == '3': #sumamos los valores del diccionario recorriendolo
        total = 0
        for cantidad in ventas_diarias.values():
            total += cantidad
        print('El total de ventas diarias es:', total)
    elif opcion == '4': #salir del programa
        print('Saliendo del programa...')
        break
    else: #si el usuario introduce otra cosa
        print('Opcion introducida no valida. Elija una opcion valida')