ventas = []
def producto_vendido(producto, precio):
    venta = {'producto':producto, 'precio':precio}
    ventas.append(venta)

def mostrar_ventas():
   for venta in  ventas:
       print('Productos', venta['producto'])
       print('Precio', venta['precio'])
       print('----')



#Ejemplos de uso
producto_vendido('Camisa', 25.99)
producto_vendido('Pantalon', 39.95)
producto_vendido('Zapatos', 61.25)

mostrar_ventas()
