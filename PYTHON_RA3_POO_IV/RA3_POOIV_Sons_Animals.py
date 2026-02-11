#Víctor Gironés Roca
#ASIX (Administració de Sistemes Informàtics en Xarxa)
#11/02/2026
#Descipcio: Polimorfisme Exercici 1: Sons d’animals 
class Animal:
    def fer_soroll(self):
        pass
    
def reproduir_soroll(self):
    print(self.fer_soroll())

class Gat(Animal):
    def fer_soroll(self):
        return "Miau"

class Vaca(Animal):
    def fer_soroll(self):
        return "Muuu"
    
gat = Gat()
vaca = Vaca()
reproduir_soroll(gat)
reproduir_soroll(vaca)
