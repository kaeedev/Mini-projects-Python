import numpy as np

ventas = np.array ([['03-01-2023', 200, 'ropa'],
                    ['09-01-2023', 87, 'alimentos'],
                    ['19-02-2023', 45, 'ropa'],
                    ['24-02-2023', 92, 'alimentos'],
                    ['03-03-2023', 355, 'ropa'],
                    ['03-03-2023', 23, 'alimentos'],
                    ['03-04-2023', 664, 'ropa'],
                    ['03-04-2023', 213, 'alimentos'],
                    ['03-05-2023', 210, 'ropa'],
                    ['03-05-2023', 34, 'alimentos'],
                    ['03-06-2023', 756, 'ropa'],
                    ['03-06-2023', 34, 'alimentos'],
                    ['03-07-2023', 12, 'ropa'],
                    ['03-07-2023', 56, 'alimentos'],
                    ['03-08-2023', 253, 'ropa'],
                    ['03-08-2023', 843, 'alimentos'],
                    ['03-09-2023', 340, 'ropa'],
                    ['03-09-2023', 29, 'alimentos'],
                    ['03-10-2023', 200, 'ropa'],
                    ['03-10-2023', 233, 'alimentos'],
                    ['03-11-2023', 123, 'ropa'],
                    ['03-11-2023', 323, 'alimentos'],
                    ['03-12-2023', 838, 'ropa'],
                    ['03-12-2023', 232, 'alimentos'],])

#extraer las fechas
fechas = np.array([venta[0] for venta in ventas])
#extraer el mes
meses = np.array([int(fecha[3:5]) for fecha in fechas])  #3:5 porque es la posicion de los numeros que nos interesa, en este caso el numero del mes
                                                        #lo convertimos a entero con int
#separamos por meses y sumamos
montos_mes = np.zeros(12) #creamos un array vacio para almacenar datos
for mes in range(1,13):   #vamos a recorrer todos los meses
    ventas_mes = ventas[meses == mes]
    montos_mes[mes-1] = np.sum(ventas_mes[:,1].astype(int)) #para convertir los numeros del array en enteros
print('Monto total de ventas por mes:', montos_mes)