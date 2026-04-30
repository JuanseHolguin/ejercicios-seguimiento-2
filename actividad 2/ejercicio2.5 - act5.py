import enum
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput
with PyCallGraph(output=GraphvizOutput):
	#, Función
    pass

class TipoCuenta(enum.Enum):
    AHORROS = 1
    CORRIENTE = 2

class Cuenta:
    nombres = ""
    apellidos = ""
    numero_cuenta = ""
    tipo_cuenta = None
    saldo = 0.0
    

    def __init__(self, numero_cuenta, nombres, apellidos, saldo, tipo_cuenta):
        self.nombres = nombres
        self.apellidos = apellidos
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta
        self.saldo = saldo

    def imprimir(self):
        print("+-----------------------------+")
        print(f"Cuenta: {self.numero_cuenta}")
        print(f"Titular: {self.nombres} {self.apellidos}")
        print(f"Tipo de Cuenta: {self.tipo_cuenta.name}")
        print(f"Saldo: {self.saldo}")

    def consultar_saldo(self):
        return print(f"El saldo actual es: {self.saldo}")

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print("+-----------------------------+")
            print(f"Se ha depositado {cantidad}. Nuevo saldo: {self.saldo}")
            print("+-----------------------------+")
            return True
        else:
            print("+-----------------------------+")
            print("La cantidad a depositar debe ser mayor que cero.")
            print("+-----------------------------+")
            return False

    def retirar(self, cantidad):
        if (cantidad > 0 and cantidad <= self.saldo):
            self.saldo -= cantidad
            print("+-----------------------------+")
            print(f"Se ha retirado {cantidad}. Nuevo saldo: {self.saldo}")
            print("+-----------------------------+")
            return True
        else:
            print("+-----------------------------+")
            print("La cantidad a retirar debe ser mayor que cero y no puede exceder el saldo actual.")
            print("+-----------------------------+")
            return False

    def mostrar_informacion(self):
        print("+-----------------------------+")
        print(f"Cuenta: {self.numero_cuenta}")
        print(f"Titular: {self.nombres} {self.apellidos}")
        print(f"Saldo: {self.saldo:.2f}")
        print("+-----------------------------+")

    def calcular_interes(self, tasa_interes):
        interes_calculado = self.saldo * (tasa_interes / 100)
        print("+-----------------------------+")
        print(f"Interés calculado a una tasa del {tasa_interes}%: {interes_calculado:.2f}")
        self.saldo += interes_calculado
        print(f"Saldo actual: {self.saldo:.2f}")
        print("+-----------------------------+")
        return interes_calculado

print("Bienvenido al sistema de gestión de cuentas bancarias.")
print("+-----------------------------+")
print("Por favor, ingrese la información de la cuenta.")
nombres = input("Ingrese los nombres del titular: ")
apellidos = input("Ingrese los apellidos del titular: ")
numero_cuenta = input("Ingrese el numero de cuenta: ")
tipo_cuenta_input = input("Ingrese el tipo de cuenta (1 para Ahorros, 2 para Corriente): ")
tipo_cuenta = TipoCuenta(int(tipo_cuenta_input))
saldo_inicial = float(input("Ingrese el saldo inicial: "))



cuenta = Cuenta(numero_cuenta, nombres, apellidos, saldo_inicial, tipo_cuenta)
cuenta.imprimir()
print("+-----------------------------+")
cuenta.depositar(float(input("Ingrese la cantidad a depositar: ")))
cuenta.retirar(float(input("Ingrese la cantidad a retirar: ")))
cuenta.calcular_interes(float(input("Ingrese la tasa de interés para calcular el interés: ")))