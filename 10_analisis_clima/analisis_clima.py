import numpy as np

clima = np.array([[12,25,67,1],
                  [8,50,54,1],
                  [6,40,90,2],
                  [4,45,56,2],
                  [17,34,45,3],
                  [19,34,21,3],
                  [20,70,12,4],
                  [22,34,90,4],
                  [23,30,23,5],
                  [12,60,57,5],
                  [23,10,67,6],
                  [22,80,77,6],
                  [40,30,47,7],
                  [38,60,57,7],
                  [38,35,17,8],
                  [34,40,27,8],
                  [31,10,57,9],
                  [30,20,37,9],
                  [24,60,57,10],
                  [22,80,47,10],
                  [22,50,27,11],
                  [18,40,37,11],
                  [12,30,47,12],
                  [11,20,87,12],])

meses = clima[:, 3] #cogemos la fecha. Será la columna de las fechas
temperaturas = clima[:,0] #cogemos la temperatura. Columna de temperaturas
humedad = clima[:,1] #cogemos la humedad. Columna de humedad
presion = clima[:,2] #cogemos la presion. Columna de presion

#creamos arrays vacios
temp_mes = np.zeros(12)
humedad_mes = np.zeros(12)
presion_mes = np.zeros(12)

#recorrer los valores para cada mes
for i in range(12):
    temp_mes[i] =np.mean(temperaturas[meses == i+1]) #decimos que pille las temperaturas donde esos meses sean igual que la operacion i+1
    presion_mes[i] =np.mean(presion[meses == i+1])
    humedad_mes[i] =np.mean(humedad[meses == i+1])
    print('La temperatura promedia en el mes', i+1, 'fue de', temp_mes[i], 'grados')
    print('La humedad promedia en el mes', i+1, 'fue de', humedad_mes[i])
    print('La presion promedia en el mes', i+1, 'fue de', presion_mes[i], 'bar')
    print('---------------')
