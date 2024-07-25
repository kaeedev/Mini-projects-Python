proyectos = {}

#agregar proyectos nuevos
proyectos['Proyecto Mariposa'] = {'Descripcion':'Descripcion1','Responsable':'Paula'}
proyectos['Proyecto Luciernaga'] = {'Descripcion':'Descripcion2','Responsable':'Teresa'}
proyectos['Proyecto Rayo'] = {'Descripcion':'Descripcion3','Responsable':'Clara'}
proyectos['Proyecto Ballena'] = {'Descripcion':'Descripcion4','Responsable': 'Alicia'}

#asignar responsables nuevos
proyectos['Proyecto Ballena']['Responsable'] = 'Elena'

#actualizar descripciones de las tareas
proyectos['Proyecto Mariposa']['Descripcion'] = 'Me gusta un monton las mariposas'
print(proyectos)

#Mostrar lista completa de tareas y responsables
print('Lista de proyectos y responsables:')
for proyecto, info in proyectos.items():
    print(f'{proyecto}. Responsable: {info['Responsable']}')



