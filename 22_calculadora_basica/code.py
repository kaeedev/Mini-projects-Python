class Calculadora:
    def __init__(self): #no tenemos que inicializar nada asi que pasamos
        pass
    def sumar(self, num1, num2):
        return num1 + num2
    def restar(self, num1, num2):
        return num1 - num2
    def multiplicar(self, num1, num2):
        return num1 * num2
    def dividir(self, num1, num2):
        if num2 == 0:
            return 'No se puede dividir por 0'
        else:
            return num1 / num2
        
mi_calculadora = Calculadora()

resultado_sumar = mi_calculadora.sumar(5,4)
resultado_restar = mi_calculadora.restar(5,4)
resultado_mult = mi_calculadora.multiplicar(5,4)
resultado_div = mi_calculadora.dividir(5,4)   

print('Resultado de la suma:', resultado_sumar)
print('Resultado de la resta:', resultado_restar)
print('Resultado de la multiplicacion:', resultado_mult)
print('Resultado de la division:', resultado_div)


