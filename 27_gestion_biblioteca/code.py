class Libro:
    def __init__(self, titulo, autor, ejemplares_disponibles):
        self.titulo = titulo
        self.autor = autor
        self.ejemplares_disponibles = ejemplares_disponibles

class Usuario:
    def __init__(self, nombre, identificacion):
        self.nombre = nombre
        self.identificacion = identificacion
        self.libros_prestados = []

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
    
    def prestar_libro(self, usuario, titulo):
        for libro in self.libros:
            if libro.titulo == titulo and libro.ejemplares_disponibles > 0:
                usuario.libros_prestados.append(libro)
                libro.ejemplares_disponibles -= 1
                print(f'El libro {titulo} ha sido prestado a {usuario.nombre}')
                return
            
        print('El ejemplar no esta disponible')

    def devolver_libro(self, usuario, titulo):
        for libro in usuario.libros_prestados:
            if libro.titulo == titulo:
                usuario.libros_prestados.remove(libro)
                libro.ejemplares_disponibles += 1
                print(f'El libro {libro.titulo} ha sido devuelto a la biblioteca por {usuario.nombre}')
    
    def mostrar_inventario(self):
        for libro in self.libros:
            print(f'{libro.titulo} de {libro.autor} -- Disponibles: {libro.ejemplares_disponibles}')


#Ejemplo de usos

biblioteca = Biblioteca()
libro1 = Libro('El gran gatsby', 'Fitzgerald', 3)
libro2 = Libro('Cien años de soledad', 'Marquez', 5)

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

usuario1 = Usuario('Lara', '12345')
usuario2 = Usuario('Ana', '54834')

biblioteca.prestar_libro(usuario1, 'El gran gatsby')
biblioteca.prestar_libro(usuario2, 'Pepe')
biblioteca.mostrar_inventario()
biblioteca.devolver_libro(usuario1, 'El gran gatsby')
biblioteca.mostrar_inventario()