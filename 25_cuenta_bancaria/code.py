
class CuentaBancaria:
    def __init__(self, numerocuenta, saldo):
        self.numerocuenta = int(numerocuenta)
        self.saldo = int(saldo)
   
    def details(self):
        print(f'Tu numero de cuenta es {self.numerocuenta} y tienes de saldo {self.saldo} €')
    
    def depositar_retirar(self):
        while True:
            opcion = int(input('Introduzca un numero para marcar una opcion: 1.Depositar 2.Retirar 3.Mostrar datos de la cuenta 4.Salir '))
            if opcion == 1:
                deposito = int(input('Cuanto quieres depositar? '))
                self.saldo += deposito
                print(f'Tu nuevo saldo es {self.saldo} €')
            if opcion == 2:
                retirar = int(input('¿Cuanto quieres retirar? '))
                if self.saldo > retirar:
                    self.saldo -= retirar
                    print(f'Tu nuevo saldo es {self.saldo} €')
                else:
                    print('No tienes dinero suficiente para retirar de tu cuenta')
            if opcion == 3:
                self.details()
            if opcion == 4:
                print('Adios')
                break
            if opcion > 4:
                print('Has introducido un opcion no valida, por favor introduzca una valida')
            

#Ejemplo de uso
mi_cuenta = CuentaBancaria(934834834, 500)
#mi_cuenta.depositar_retirar()








