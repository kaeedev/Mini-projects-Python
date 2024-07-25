asistencias_alumnos = {}

#agregamos asistencias de los estudiantes

asistencias_alumnos['Manolo'] = ['01-04-2023','02-05-2023','23-05-2023']
asistencias_alumnos['Juan'] = ['01-06-2023','02-08-2023','23-12-2023']
asistencias_alumnos['Mireia'] = ['06-09-2023','22-10-2023','31-12-2023']

#agregar nuevas fechas de asistencia a los estudiantes. Al ser listas las fechas usaremos append

asistencias_alumnos['Mireia'].append('23-01-2024')
asistencias_alumnos['Manolo'].append('29-04-2024')

#Lista total
print('Lista de estudiantes con sus fechas de asistencias:')
for alumnos, fechas in asistencias_alumnos.items():
    print(f'El alumno {alumnos} ha asistido en las siguientes fechas a las clases: {fechas}')
