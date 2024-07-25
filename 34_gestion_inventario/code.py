def busqueda_binaria_recursiva(inventario, codigo, inicio, fin):
    # Caso base: Si el inicio es mayor que el fin, el elemento no está presente en el inventario
    if inicio > fin:
        return 0

    # Calculamos el punto medio del rango actual
    medio = (inicio + fin) // 2

    # Comprobamos si el código del producto en el punto medio es el que estamos buscando
    if inventario[medio]['codigo'] == codigo:
        return inventario[medio]['cantidad']
    # Si el código del producto en el punto medio es mayor que el código buscado,
    # buscamos en la mitad izquierda del rango
    elif inventario[medio]['codigo'] > codigo:
        return busqueda_binaria_recursiva(inventario, codigo, inicio, medio - 1)
    # Si el código del producto en el punto medio es menor que el código buscado,
    # buscamos en la mitad derecha del rango
    else:
        return busqueda_binaria_recursiva(inventario, codigo, medio + 1, fin)

def buscar_cantidad(inventario, codigo):
    # Llamamos a la función de búsqueda binaria recursiva
    # con los índices de inicio y fin del inventario
    cantidad = busqueda_binaria_recursiva(inventario, codigo, 0, len(inventario) - 1)
    return cantidad

# Ejemplo de uso:
inventario = [
    {'codigo': 101, 'cantidad': 50},
    {'codigo': 202, 'cantidad': 100},
    {'codigo': 303, 'cantidad': 75},
    {'codigo': 404, 'cantidad': 200},
    {'codigo': 505, 'cantidad': 150}
]

codigo_buscar = 303
cantidad_disponible = buscar_cantidad(inventario, codigo_buscar)
print(f"La cantidad disponible para el producto con código {codigo_buscar} es: {cantidad_disponible}")
