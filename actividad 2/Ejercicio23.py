class automovil:
    def __init__(self, marca, modelo, motor, tipo_combustible, tipo_automovil, no_puertas, no_asientos, vel_max, color):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.tipo_combustible = tipo_combustible
        self.tipo_automovil = tipo_automovil
        self.no_puertas = no_puertas
        self.no_asientos = no_asientos
        self.vel_max = vel_max
        self.color = color
        self.vel_actual = 0
    #GET
    def get_vel_actual(self):
        return self.vel_actual
    #SET
    def set_vel_actual(self, velocidad):
        self.vel_actual = velocidad
    
    def acelerar (self, incremento):
        if self.vel_actual + incremento > self.vel_max:
            print ("El automovil no puede superar la vel_max")
        else: 
          self.vel_actual += incremento
          print(f"La velocidad actual es de : {self.vel_actual} km/h")   
    def desacelerar (self, disminucion):
        if self.vel_actual - disminucion < 0 :
            print ("El automovil no puede tener velocidad negativa")
        else: 
            self.vel_actual -= disminucion
            print(f"La velocidad actual es de : {self.vel_actual} km/h")
    def calcular_llegada (self, distancia):
        if self.vel_actual == 0:
            print ("El vehiculo esta detenido")
        else: 
            return distancia/self.vel_actual
    def frenar(self):
        self.vel_actual = 0
        print("El automóvil ha frenado. Velocidad actual: 0 km/h")
    def mostrar_datos(self):
        print("----- Datos del Automóvil -----")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Motor: {self.motor} L")
        print(f"Combustible: {self.tipo_combustible}")
        print(f"Tipo: {self.tipo_automovil}")
        print(f"Puertas: {self.no_puertas}")
        print(f"Asientos: {self.no_asientos}")
        print(f"Velocidad Máxima: {self.vel_max} km/h")
        print(f"Color: {self.color}")
        print(f"Velocidad Actual: {self.vel_actual} km/h")
        print("--------------------------------")
automovil = automovil("Toyota", 2022, 1.8, "Gasolina", "SUV", 4, 5, 200, "Gris Oscuro")
automovil.mostrar_datos()
automovil.set_vel_actual(100)
tiempo = automovil.calcular_llegada(60)
print (f"El tiempo de llegada es de {tiempo:.2f} horas ")
print(f"Velocidad actual: {automovil.get_vel_actual()} km/h")

automovil.acelerar(20)
automovil.desacelerar(50)
automovil.frenar()



    
    

