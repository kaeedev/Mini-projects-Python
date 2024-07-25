
class Vuelo:
    def __init__(self, numero_vuelo, origen, destino, capacidad):
        self.numero_vuelo = numero_vuelo
        self.origen = origen
        self.destino = destino
        self.capacidad = capacidad
        self.pasajeros = []

    def disponibilidad_asiento(self):
            return(self.capacidad - len(self.pasajeros))
        
    def agregar_pasajeros(self, pasajeros):
        if self.disponibilidad_asiento() > 0: #podemos llamar a un metodo dentro de otro metodo
            self.pasajeros.append(pasajeros)
            print(f'Pasajero {pasajeros} agregado al vuelo {self.numero_vuelo}')

class VueloEspecial(Vuelo):
     def __init__(self, numero_vuelo, origen, destino, capacidad, motivo):
          super().__init__(numero_vuelo,origen,destino,capacidad)
          self.motivo = motivo

#Ejemplos de uso

mi_vuelo = Vuelo(83894, 'Malaga', 'Madrid', 0)
mi_vuelo2 = Vuelo(22234, 'Brasil', 'Argentina', 24)
mi_vuelo.agregar_pasajeros('Laura')
mi_vuelo2.agregar_pasajeros('Silvia')
print('Asientos disponibles:', mi_vuelo.disponibilidad_asiento())

vuelo_especial = VueloEspecial(3443, 'Miami', 'Barcelona', 100, 'Vacaciones')
vuelo_especial.agregar_pasajeros('Antonio')
print('Asientos disponibles en el vuelo especial:', vuelo_especial.disponibilidad_asiento())
print('Motivo del vuelo especial:', vuelo_especial.motivo)
