nombres_contraseñas = [['juan123','clave123'],['ana456','clave456'],['pedro789','clave789']]


nombre_introducido= input('Introduce el nombre de usuario: ')
contraseña_introducida = input('Introduce tu contraseña: ')
usuario_valido = False
for nombre, contraseña in nombres_contraseñas:
    if nombre == nombre_introducido and contraseña == contraseña_introducida:
        usuario_valido = True
        break
if usuario_valido:
    print(f'Bienvenido {nombre}')
else:
    print('Usuario o contraseña incorrectos')


