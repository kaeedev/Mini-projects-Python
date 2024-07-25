class ListaTarea:
    def __init__(self):  #iniciamos una lista
        self.tareas = []

    def agregar_tareas(self, tareas):  #funcion para agregar un diccionario con pares a la lista inicial. Iniciamos completada como false porque primero la tarea estara pendiente
        self.tareas.append({'tarea': tareas,'completada':False})

    def marcar_completada(self, indice): #funcion que al indicar el indice, ponga completada en el par clave valor del diccionario
        if 0 <= indice < len(self.tareas):
            self.tareas[indice]['completada'] = True
        else:
            print('Indice invalido')

    def mostrar_tareas(self): #funcion para imprimir las tareas completadas o pendientes
        if not self.tareas:
            print('No hay tareas pendientes')
        else:
            print('Tareas pendientes: ')
            for i, tarea in enumerate(self.tareas):  #enumerate se usa para iterar sobre una secuencia y que lleve a la vez un registro del indice de cada elemento
                estado = 'Completada' if tarea['completada'] else 'Pendiente' #si tarea completada es true el valor de estado sera completado, sino pendiente
                print(f"{i + 1}. [{estado}] {tarea['tarea']}") #i + 1 es i es el indice y se le suma 1 para que no empiece en 0

#ejemplos de uso
lista = ListaTarea()
print('Para marcar una tarea completada, indicalo con su numero')
lista.agregar_tareas('Hacer la compra')
lista.agregar_tareas('Hacer deberes')
lista.agregar_tareas('Jugar al lol')
lista.agregar_tareas('Comprar pan')
lista.mostrar_tareas()
lista.marcar_completada(2)
lista.mostrar_tareas()