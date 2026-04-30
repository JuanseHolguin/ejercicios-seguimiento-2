class persona:
    def __init__(self, nombre, apellido, documento, añoNacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.añoNacimiento = añoNacimiento

    
    def impresion(self):
        print(f"Nombre = {self.nombre}")
        print(f"Apellido = {self.apellido}")
        print(f"Numero de documento = {self.documento}")
        print(f"Año de nacimiento = {self.añoNacimiento}")



    nombre = input("ingrese el nombre de la persona: ")
    apellido = input("ingrese el apellido de la persona: ")
    documento = input("ingrese el documento de la persona: ")
    año = int(input("ingrese el año de nacimiento de la persona: "))

    

p1 = persona(persona.nombre, persona.apellido, persona.documento, persona.año)
p1.impresion()


