import numpy as np

datos = np.array ([['2021-01-01', 'Componente 1', 'Lote A', 80],
                   ['2021-01-15', 'Componente 1', 'Lote B', 90],
                   ['2021-02-01', 'Componente 2', 'Lote C', 85],
                   ['2021-02-15', 'Componente 2', 'Lote D', 95],
                   ['2021-03-01', 'Componente 1', 'Lote E', 75],
                   ['2021-03-15', 'Componente 2', 'Lote F', 90]])

#----componente calidad mas alta
#seleccionamos los tipos de componentes
tipos_componente = datos[:,1]
#encontramos los componentes unicos
tipos_unicos = np.unique(tipos_componente)
#convertimos los numeros string en float
calidad = datos[:,3].astype(float)
#creamos un array vacio para almacenar los promedios con la longitud de los componentes que hay
promedios = np.zeros(len(tipos_unicos))
#iteramos sobre los tipos unicos de componentes
i = 0
for tipo in tipos_unicos:
    promedios[i] = np.mean(calidad[tipos_componente == tipo]) #esta linea calcula el promedio de la calidad de todos los componentes que tienen el mismo tipo
    i = i + 1
indice_maximo = np.argmax(promedios) #funcion para encontrar el indice del valor mas alto
tipo_mejor_calidad = tipos_unicos[indice_maximo]
print('El tipo de componente con la puntuacion de calidad mas alta es:',tipo_mejor_calidad)


#---- encontrar cuantos componentes se produjeron en cada mes
#extraemos las fechas
fechas = datos[:,0]
#extraemos los meses y hacemos el conteo
meses, counts = np.unique([fecha[0:7] for fecha in fechas], return_counts = True)
print(meses)
for i in range(len(meses)):
    print('Mes:', meses[i], 'Cantidad producida', counts[i])

#----- puntuacion de calidad promedio de los componentes
promedio_tipo = np.zeros(len(tipos_unicos))
for i in range(len(tipos_unicos)):
    promedio_tipo[i] = np.mean(calidad[tipos_componente == tipos_unicos[i]]) #Cogemos los valores de calidad de los componentes que nos interesan
    print('La puntuacion de calidad promedio para el', tipos_unicos[i], 'es:', promedio_tipo[i])

