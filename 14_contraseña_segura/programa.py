import validador
import creador

#PROGRAMA PARA PEDIR CONTRASEÑA, SE VALIDARA SI ES SEGURA Y SI NO SE CREARA UNA ALEATORIA SEGURA

def main(): #funcion main contiene la logica principal del programa. Es la funcion principal
    contrasena = input('Ingrese una contraseña: ')
    if validador.validar_contrasena(contrasena):
        print('La contraseña es segura')
    else:
        print('La contraseña no cumple con los requisitos minimos de seguridad')
        nueva_contrasena = creador.generador_contrasena(8)
        print('Nueva contraseña sugerida:', nueva_contrasena)

if __name__ == '__main__': #esto es para definir que lo que se esta ejecutando aqui es el programa principal
    main()