

class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion



#ejemplos de usos
persona1 = Persona('Luis', '24', 'Estudiante')
persona2 = Persona('Mireia', '20', 'Estudiante')
persona3 = Persona ('Xuxo', '20', 'Nini')

print(persona1.nombre, persona1.edad, persona1.profesion)
print(persona2.nombre, persona2.edad, persona2.profesion)
print(persona3.nombre, persona3.edad, persona3.profesion)