#--- Hacemos que el usuario introduzca sus datos
genero = input('¿Eres chico o chica?: ')
nombre = input('Indica tu nombre: ')
nombres_chicas_A = 'EFGHIJKLM'
nombres_chicos_A = 'ABCDEFGHRSTUVWXYZ'

if genero.lower() == 'chica':
    if nombre[0].upper() in nombres_chicas_A: #Con esto podemos coger la primera posicion de un string en mayuscula en la variable que indiquemos
        print('Estas en el grupo A')
    else:
        print('Estas en el grupo B')
elif genero.lower() == 'chico':
    if nombre[0].upper() in nombres_chicos_A:
        print('Estas en el grupo A')
    else: 
        print('Estas en el grupo B')
else:
    print('Introduce un genero valido')