import enum

class TipoPlaneta(enum.Enum):
    GASEOSO = "Gaseoso"
    TERRESTRE = "Terrestre"
    ENANO = "Enano"

class planeta:
    nombre = ""
    CantidadSatelites = 0
    masa = 0
    diametro = 0
    distanciasol = 0
    esObservable = False
    volumen = 0
    periodoOrbital = 0
    periodorotacional = 0

    def __init__(self, nombre, CantidadSatelites, masa, volumen, diametro, distanciasol, tipoPlaneta, esObservable, periodoOrbital, periodorotacional):
        self.nombre = nombre
        self.CantidadSatelites = CantidadSatelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distanciasol = distanciasol
        self.tipoPlaneta = tipoPlaneta
        self.esObservable = esObservable
        self.periodoOrbital = periodoOrbital
        self.periodorotacional = periodorotacional

    def densidad(self):
        return self.masa/self.volumen
    
    def esplanetaExterior(self):
        limite = (149597870 * 3.4)

        if self.distanciasol > limite:
            return True
        else:            return False  

    def imprimir(self):
        print("+-----------------------------+")
        print("Nombre: ", self.nombre)
        print("Cantidad de Satelites: ", self.CantidadSatelites)
        print("Masa: ", self.masa)
        print("Volumen: ", self.volumen)
        print("Diametro: ", self.diametro)
        print("Distancia al Sol: ", self.distanciasol)
        print("Tipo de Planeta: ", self.tipoPlaneta)
        print("Es Observable: ", self.esObservable)
        print("Densidad: ", self.densidad())
        print("Es planeta exterior: ", self.esplanetaExterior())
        print("Periodo Orbital: ", self.periodoOrbital)
        print("Periodo Rotacional: ", self.periodorotacional)
        print("+-----------------------------+")

nombre = input("Ingrese el nombre del planeta: ")
CantidadSatelites = int(input("Ingrese la cantidad de satelites: "))
masa = float(input("Ingrese la masa del planeta: "))
volumen = float(input("Ingrese el volumen del planeta: "))
diametro = float(input("Ingrese el diametro del planeta: "))
distanciasol = float(input("Ingrese la distancia al sol del planeta: "))
tipoPlaneta = input("Ingrese el tipo de planeta (gaseoso, terrestre, enano): ")
periodoOrbital = float(input("Ingrese el periodo orbital del planeta: "))
periodorotacional = float(input("Ingrese el periodo rotacional del planeta: "))

p1 = planeta(nombre, CantidadSatelites, masa, volumen, diametro, distanciasol, tipoPlaneta, True, periodoOrbital, periodorotacional)
p1.imprimir()
    
