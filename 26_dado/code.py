

import random

class Dado:
    def __init__(self, lanzamiento):
        self.lanzamiento = lanzamiento
    def details(self):
        print(f'El numero que ha salido al tirar el dado es {self.lanzamiento}')

#ejemplo de uso
mi_dado = Dado(random.randint(1,6))
#mi_dado.details()