#Víctor Gironés Roca
#ASIX (Administració de Sistemes Informàtics en Xarxa)
#11/02/2026
#Descipcio: Exercici 2: Vehicles

class Vehicle:
    def __init__(self, marca):
        self.marca = marca
        
    def arrencar(self):
        print(f"{self.marca} està arrencant.")
        
class Cotxe(Vehicle):
    def tocar_claxon(self):
        print("Pip pip!")

cotxe = Cotxe("Toyota")
cotxe.arrencar()
cotxe.tocar_claxon()    

