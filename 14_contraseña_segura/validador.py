#ESTA FUNCION VALIDA SI LA CONTRASEÑA INTRODUCIDA EN EL PROGRAMA PRINCIPAL CUMPLE LOS REQUISITOS MINIMOS

import re #modulo de phyton para buscar patrones dentro de una cadena
def validar_contrasena(contrasena):
    #Requisitos minimos: longitud minima de 8 caracteres, al menos una mayuscula y una minuscula, un numero y un caracter especial
    long = 8
    if len(contrasena) < long:
        return False
    if not re.search(r'[A-Z]', contrasena): #valida si hay una mayuscula en el string
        return False
    if not re.search(r'[a-z]', contrasena): # valida si hay una minuscula en el string
        return False
    if not re.search(r'\d', contrasena): #valida si hay algun digito en el string. Se representa con r"\d"
        return False
    if not re.search(r'[!@#$^&*()-+=]', contrasena): # valida si hay algun caracter especial en el string
        return False
    
    return True