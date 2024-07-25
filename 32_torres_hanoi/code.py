def mover_disco(desde, hacia, disco):
    print(f'Mover disco {disco} de la torre {desde} hacia la torre {hacia}')

def torres_de_hanoi(n, origen, destino, auxiliar):
    #caso base
    if n == 1:
        mover_disco(origen, destino, n)
        return
    
    torres_de_hanoi(n - 1, origen, auxiliar, destino)
    mover_disco(origen, destino, n)
    torres_de_hanoi(n-1,auxiliar,destino,origen)


torres_de_hanoi(5, 'Origen', 'Destino', 'Auxiliar')