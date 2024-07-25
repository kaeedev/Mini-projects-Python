
#Pedimos un nombre
nombre= input('Indique su nombre ')
print('Hola ' + str(nombre.title()))
print(' ')

#Calculamos el salario semanal dinero x horas
horas= input('¿Cuantas horas has trabajado en la semana? ')
dineroH= input('¿Cuanto dinero ganas por hora? ')
salarioSemanal = float(horas)*float(dineroH)
print('Tu salario semanal es de: ' + str(salarioSemanal)+'€')

print(' ')

 #Calculamos el salario anual por 52 ya que es el numero de semanas que tiene un año aproximadamente
salarioAnual= float(salarioSemanal)*52
print('Tu salario anual es de: ' + str(salarioAnual)+ '€')

print(' ')

#Pedimos los gastos semanales
gastos= input('¿Cuanto gastas a la semana? ')
gastosSemanales= float(salarioSemanal) - float(gastos)
print('A la semana te quedarias con: ' + str(gastosSemanales) + '€')

print(' ')

#Calculamos el gasto anual por 52 que son todas las semanas del año
gastosAnual= float(gastos) * 52
print('Tienes un gasto anual de: '+ str(gastosAnual)+ '€')

print(' ')

#Calculamos lo que ahorra al año restando el salario menos los gastos
ahorroAnualTotal= float(salarioAnual)-float(gastosAnual)
print('Ahorras al año: ' + str(ahorroAnualTotal) + '€')
