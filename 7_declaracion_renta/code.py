#--- Pedimos datos por pantalla
edad = int(input('Introduce tu edad: '))
salario = float(input('¿Cuanto cobras al mes?: '))

#--- Hacemos las condicionales para que nos indique que tipo impositivo nos tocaria
if (edad >= 18) and (salario > 1000):
    if salario < 15000:
        print('Eres susceptible de que se te aplique un tipo impositivo, concretamente el del 5%')
    elif salario >= 15000 and salario <= 25000:
        print('Eres susceptible de que se te aplique un tipo impositivo, concretamente el del 15%')
    elif salario >= 25000 and salario <= 35000:
        print('Eres susceptible de que se te aplique un tipo impositivo, concretamente el del 20%')
    elif salario >= 35000 and salario <= 60000:
        print('Eres susceptible de que se te aplique un tipo impositivo, concretamente el del 30%')
    else:
        print('Eres susceptible de que se te aplique un tipo impositivo, concretamente el del 45%')
else:
    print('No cumples con los requisitos para que seas susceptible de que se te aplique algun tipo impositivo')