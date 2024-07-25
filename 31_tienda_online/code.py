
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

class Tienda:
    def __init__(self):
        self.productos = []

    def agregar_productos(self, producto):
        self.productos.append(producto)

    def mostrar_inventario(self):
        for producto in self.productos:
            print(f'{producto.nombre} - Precio: {producto.precio} € - Cantidad : {producto.cantidad}')
        
    def comprar_producto(self, nombre, cantidad):
        for producto in self.productos: #recorremos la lista
            if producto.nombre == nombre: #comprobamos que el nombre que queremos esta en la lista
                if producto.cantidad >= cantidad: #comprobamos si hay la cantidad suficiente
                    producto.cantidad -= cantidad #si la hay que reste esa cantidad a la cantidad que existe
                    print(f'Compra exitosa. Total: {producto.precio * cantidad}€')  #el precio lo multiplicamos por la cantidad que compremos
                else:
                    print('No hay suficiente cantidad')
                return #salimos de la funcion para que no imprima el print de abajo
            
        print('Producto no encontrado')
        

#Usos

tienda = Tienda()
producto1 = Producto('Camiseta', 20, 50)
producto2 = Producto('Pantalon', 30, 30)
tienda.agregar_productos(producto1)
tienda.agregar_productos(producto2)
tienda.mostrar_inventario()

tienda.comprar_producto('Camiseta', 2)
tienda.mostrar_inventario()