def contar_palabras(archivo, palabra_a_buscar): #funcion para contar palabras repetidas en un texto
    try:

        with open(archivo) as file:   #abrimos el archivo y que lea el contenido
            contenido = file.read()
            contenido_minuscula = contenido.lower() #hacemos que el texto se convierta en minuscula
            palabra_a_buscar = palabra_a_buscar.lower() #hacemos que la palabra que introduzcamos para buscar sea insensible a mayusc/minusc
            palabras = contenido_minuscula.split() #indicamos que las palabras estan divididas por espacios con split
            ocurrencias = palabras.count(palabra_a_buscar) #count contara el numero de veces que aparece la palabra que introduzcamos
            return ocurrencias
    except FileNotFoundError:
        print('El archivo que quieres analizar no existe') #Manejamos el error por si no encuentra el archivo
        return 0


archivo = input('Que archivo quieres analizar? ')
palabra = input('Que palabra quieres averiguar cuantas veces sale? ')

conteo = contar_palabras(archivo, palabra)  #llamamos a la funcion con argumentos los dos inputs
if conteo > 0: #si el conteo es mas que 0, indicara cuantas veces encontró la palabra dentro del texto
    print(f'La palabra {palabra} aparece {conteo} veces en el archivo {archivo}')
else: #si no encuentra ocurrencia
    print('No se encontraron ocurrencias de la palabra introducida')
