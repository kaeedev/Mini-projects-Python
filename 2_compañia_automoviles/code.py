
#Preguntamos cuantos RBM Serie 1 ha vendido y calculamos la ganancia total
cantidad_RbmSerie1 = int(input('¿Cuantos RBM Serie 1 has vendido este mes? '))
rbm_Serie1 = 20000
venta_rbmSerie1 = cantidad_RbmSerie1 * rbm_Serie1
print(str(venta_rbmSerie1) + '€')
#Calculamos la comisión que gana el vendedor por la venta de todos los RBM Serie 1 en el mes
comision_rbmSerie1 = venta_rbmSerie1 * 0.03
print(str(comision_rbmSerie1) + '€. Esta es la comision del mes por la venta de los RBM Serie 1')
print(' ')

#Preguntamos cuantos RMB Serie Plus ha vendido y calculamos la ganancia total
cantidad_RmbSeriePlus = int(input('¿Cuantos RMB Serie Plus has vendido este mes? '))
rmb_SeriePlus = 35000
venta_rmbSeriePlus = cantidad_RmbSeriePlus * rmb_SeriePlus
print(str(venta_rmbSeriePlus) + '€')
#Calculamos la comision que gana el vendedor por la venta de todos los RMB Serie Plus en el mes
comision_rbmSeriePlus = venta_rmbSeriePlus * 0.05
print(str(comision_rbmSeriePlus) + '€. Esta es la comision del mes por la venta de los RMB Serie Plus')
print(' ')

#Preguntamos cuantos RBM todoterreno ha vendido y calculamos la ganancia total
cantidad_RbmTodoterreno = int(input('¿Cuantos RBM todoterreno has vendido este mes? '))
rbm_todoterreno = 60000
venta_rbmTodoterreno = cantidad_RbmTodoterreno * rbm_todoterreno
print(str(venta_rbmTodoterreno) + '€')
#Calculamos la comision que gana el vendedor por la venta de todos los RBM todoterreno en el mes
comision_rbmTodoterrenos = venta_rbmTodoterreno * 0.07
print(str(comision_rbmTodoterrenos) + '€. Esta es la comision del mes por la venta de los RBM todoterreno')
print(' ')
#Calculamos el total de lo que va a ganar en el mes por comisiones

comisiones_Totales = comision_rbmSerie1 + comision_rbmSeriePlus + comision_rbmTodoterrenos
print('Tu ganancia total en comisiones en este mes es de: ' + str(comisiones_Totales) + '€')
