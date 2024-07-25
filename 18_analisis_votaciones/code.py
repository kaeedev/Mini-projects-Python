elecciones = {}

while True:
    opcion = input('1.Agregar candidatos 2.Mostrar la lista de candidatos 3.Encontrar candidato ganador 4.Calcular porcentaje de votos 5.Salir: ')
    if opcion == '1':
        candidato = input('Ingrese el nombre del candidato: ')
        votos = int(input('Ingrese el numero de votos: '))
        if candidato in elecciones:
            elecciones[candidato] += votos
        else:
            elecciones[candidato] = votos
    elif opcion == '2':
        for candidato, votos in elecciones.items():
            print('El candidato', candidato, 'tiene:', votos, 'votos')
    elif opcion == '3':
        candidato_ganador = max(elecciones, key=elecciones.get)
        print('El ganador de las elecciones es:', candidato_ganador)
    elif opcion == '4':
        suma_votos = sum(elecciones.values())
        for candidato, votos in elecciones.items():
            porcentaje = (votos / suma_votos) * 100
            print(f'El porcentaje de votos para {candidato} es: {porcentaje:.2f}%')
    elif opcion == '5':
        print('Saliendo del programa')
        break
    else:
        print('La opcion introducida es invalida, introduzca una valida')


