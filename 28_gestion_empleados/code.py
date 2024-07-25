class Empleado:
    def __init__(self, nombre, apellido, salario_base):
        self.nombre = nombre
        self.apellido = apellido
        self.salario_base = salario_base
    
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, apellido, salario_base, bono_anual):
        super().__init__(nombre, apellido, salario_base)
        self.bono_anual = bono_anual

    def calcular_salario_total(self):
        return(self.salario_base + self.bono_anual)

class EmpleadoTiempoParcial(Empleado):
    def __init__(self, nombre, apellido, salario_base, horas_trabajadas):
        super().__init__(nombre, apellido, salario_base)
        self.horas_trabajadas = horas_trabajadas

    def calcular_salario_total(self):
        return(self.salario_base + 1.5*self.horas_trabajadas*4*12) #suplemento de horas trabajadas por las semanas de un año
    

#ejemplos de uso
empleado_tiempo_completo = EmpleadoTiempoCompleto('Juan', 'Rodriguez', 1200, 2500)
print('El salario total del empleado a tiempo completo con su bono es:', empleado_tiempo_completo.calcular_salario_total())

empleado_tiempo_parcial = EmpleadoTiempoParcial('Manolo', 'Ortiz', 700, 25)
print('El salario total del empleado a tiempo parcial es:', empleado_tiempo_parcial.calcular_salario_total())