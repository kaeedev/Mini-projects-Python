class Coche:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.encendido = False  #Booleano
    def details(self):
        print(f'El coche es de la marca {self.marca}, concretamente modelo {self.modelo} del año {self.año}')
    def encender(self):
        if not self.encendido: #Forma de verificar si la variable es False. Not invierte el valor de verdad de un booleano
            self.encendido = True
            print('El coche ha sido encendido')
        else:
            print('El coche ya esta encendido')
    def apagar(self):
        if self.encendido:
            self.encendido = False
            print('El coche ha sido apagado')
        else:
            print('El coche ya esta apagado')



#Ejemplos de uso
mi_coche = Coche('Audi', 'A300', '2006')
mi_coche.details()

mi_coche.encender()
mi_coche.encender()
mi_coche.apagar()
mi_coche.apagar()