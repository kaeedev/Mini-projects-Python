def validar_formulario(nombre,numero,correo):
    if len(nombre)< 3:
        print('Nombre invalido, debes introducir minimo un nombre de 3 caracteres')
    else:
        print(nombre)
    if len(numero)< 9:
        print('Numero invalido, debes introducir un numero de 9 digitos')
    else:
        print(numero)
    if '@' not in correo or '.' not in correo:
        print('Correo invalido, debe contener @ y .')
    else:
        print(correo)

#Ejemplo de uso
validar_formulario('Juan', '123456231','lal.com')