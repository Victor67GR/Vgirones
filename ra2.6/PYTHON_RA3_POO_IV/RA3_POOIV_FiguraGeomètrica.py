#Víctor Gironés Roca
#ASIX (Administració de Sistemes Informàtics en Xarxa)
#11/02/2026
#Descipcio: Exercici 4: Figura geomètrica 

import math
class Figura:
    def area(self):
        print("Àrea no definida.")

class Quadrat(Figura):
    def __init__(self, costat):
        self.costat = costat
        
    def area(self):
        return self.costat ** 2
    
class Cercle(Figura):
    def __init__(self, radi):
        self.radi = radi
        
    def area(self):
        return math.pi * (self.radi ** 2)
    
quadrat = Quadrat(4)
cercle = Cercle(3)

print(f"Área del quadrat: {quadrat.area()}")
print(f"Área del cercle: {cercle.area()}")


