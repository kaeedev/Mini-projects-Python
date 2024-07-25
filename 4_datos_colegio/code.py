
#Nuestra base de datos
estudiantes = ['Juan','Maria','Pedro']
database = []
for estudiante in estudiantes:
    notas = []
    print(f'Ingrese las notas de {estudiante}')
    deberes = float(input('Notas de deberes: '))
    notas.append(deberes)
    examenes = float(input('Notas de examenes: '))
    notas.append(examenes)
    proyectos = float(input('Notas de proyectos: '))
    notas.append(proyectos)
    database.append([estudiante, notas])


#Calcular la nota media de cada estudiante
sum_media = 0
for data in database:
    nombre = data[0] #extraemos el nombre del estudiante
    notas = data[1] #extraemos la lista de notas
    suma_notas = 0
    for nota in notas:
        suma_notas = suma_notas + nota
        media = suma_notas/len(notas)

    print(f'La media de {nombre} es {media :.2f}') #la f cambia el formato, podemos poner variables dentro de la string usando {}
    #:.2f es una funcion para limitar los numeros decimales solo 2 cifras despues de la coma, para que los numeros no sean tan largos

    sum_media = sum_media + media   #calculamos la media de toda la clase
media_clase = sum_media/len(database) #calculamos la media de toda la clase
print(f'La media de la clase es {media_clase :.2f}')