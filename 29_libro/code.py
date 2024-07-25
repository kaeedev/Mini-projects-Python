class Libro:
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año
    def details(self):
        print(f'El libro {self.titulo} tiene como autor a {self.autor} y fue creado en {self.año}')


#Ejemplos de uso
libro1 = Libro('La vida de Mireia', 'Kae', '1999')
libro2 = Libro('Las aventuras de LOL300', 'Corpiñas', '2024')
libro3 = Libro('Smash bros malaga', 'Yato', '2023')

libro1.details()
libro2.details()
libro3.details()