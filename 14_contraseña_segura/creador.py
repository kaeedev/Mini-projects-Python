import random #modulo de phyton que proporciona funciones para generar numeros pseudoaleatorios
import string #modulo en phyton que proporciona varias constantes utiles y funciones con las cadenas de texto

#ESTA FUNCION CREA UNA CONTRASEÑA ALEATORIA AL DAR EL USUARIO UNA CONTRASEÑA INVALIDA. LE SUGIERE UNA CONTRASEÑA VALIDA BASANDOSE EN LOS REQUISITOS
def generador_contrasena(longitud, incluir_mayusculas = True, incluir_minusculas = True, incluir_numeros = True, incluir_especiales = True):
    caracteres = ''
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase #es una constante del modulo string que contiene todas las letras en mayuscula de la A a la Z. Esto lo que hara es añadir una mayuscula aleatoria
    if incluir_minusculas:
        caracteres += string.ascii_lowercase #igual que la anterior pero con minusculas
    if incluir_numeros:
        caracteres += string.digits # lo mismo pero con numeros
    if incluir_especiales:
        caracteres += string.punctuation #lo mismo pero generando simbolos de puntuacion y especiales

    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud)) #esto genera de forma random una contraseña gracias a random.choice segun lo proporcionado en caracteres
    return contrasena                                                        #join concatena cada caracter aleatorio seleccionado en una cadena
                                                                            #genera una contraseña aleatoria de longitud 'longitud' utilizando caracteres especificados en la variable 'caracteres'