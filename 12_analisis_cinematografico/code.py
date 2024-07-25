import numpy as np

peliculas = np.array([['Peli 1', 'Comedia', 120, 1990, 8.5],
                      ['Peli 2', 'Accion', 110, 2005, 7.8],
                      ['Peli 3', 'Drama', 95, 2010, 6.9],
                      ['Peli 4', 'Comedia', 100, 1985, 7.5],
                      ['Peli 5', 'Accion', 130, 2015, 8.1],
                      ['Peli 6', 'Drama', 115, 2000, 6.7],
                      ['Peli 7', 'Comedia', 90, 1995, 8.2],
                      ['Peli 8', 'Accion', 105, 2010, 7.4],
                      ['Peli 9', 'Drama', 125, 1980, 6.8],
                      ['Peli 10', 'Comedia', 95, 2000, 8.0],])

#----genero mas popular

generos, conteos= np.unique(peliculas[:,1], return_counts = True) #Elegimos la columna de generos y .unique nos devuelve los elementos unicos, no los repetidos
                                                   #np.unique tambien nos da la opcion de mostrar cuantas veces aparece cada elemento, para eso usamos el return_counts
                                                   #para guardar el conteo debemos asignar una nueva variable, en este caso conteos
                                                                  #con esto sabremos cuantas veces aparece cada generos
                                                                
#ordenamos los conteos de mayor a menor
conteos_desc = np.argsort(conteos)[::-1] #esto nos devuelve los indices de los elementos del array conteos de mayor a menor


#extraer el genero mas popular
genero_popular = generos[conteos_desc[0]] #el primer elemento de los conteos es el mayor
print('El genero mas popular es:', genero_popular)


#----agrupamos las peliculas por decada

print(peliculas[:,3])
decadas = np.unique(peliculas[:,3].astype(int) //10 * 10) #convertimos a int las fechas. Con // lo que hacemos es redondear numeros. Si ponemos 10 redondeara a decadas y * 10 para el año q nos interesa para que nos de un numero de 4 cifras
print(decadas)

#contamos las peliculas en cada decada
conteos_decadas = []
for decada in decadas:
    conteo = np.count_nonzero((peliculas[:,3].astype(int)>= decada) & (peliculas[:,3].astype(int) < decada + 10)) #Hacemos que cuente los elementos entre decadas. Con esta funcion seleccionamos que elementos queremos que se cuenten para calcular
    conteos_decadas.append(conteo)
    print('En la decada de', decada, 'se crearon', conteo, 'peliculas')

#---- duracion promedio por genero

todos_generos = peliculas[:,1]
duraciones = peliculas[:,2]
duracion_media = np.zeros(len(generos)) #para que tenga la longitud de los generos ya vistos antes
for i in range(len(generos)):
    print(generos[i])
    duracion_media[i] = np.mean(duraciones[todos_generos == generos[i]].astype(float)) #para que solo trate los generos del loop. Los convertimos en float para que no sean strings los numeros
    print('Duracion media de las peliculas:', generos[i], 'es de', duracion_media[i], 'minutos')