
#--- Pedimos por consola el nombre, la edad y la nota media
nombre = input('Escribe tu nombre: ')
edad = int(input('Escribe tu edad: '))
nota_media = float(input('Escribe tu nota media: '))
#--- Reemplazamos por si se equivoca el usuario al poner el nombre
nombre = nombre.replace('.','')
nombre = nombre.replace(',','')
nombre = nombre.replace('#','')
nombre = nombre.replace('*','')
nombre = nombre.lower()
#--- Ponemos los requisitos minimos para optar a beca
if (edad >= 17 and edad <= 21) and (nota_media >= 8):
    print('Si puedes optar a la beca,', nombre.title())
else:
    print('No puedes optar a la beca ya que te faltan algunos requisitos,', nombre.title())