#Víctor Gironés Roca
#ASIX (Administració de Sistemes Informàtics en Xarxa)
#11/02/2026
#Descipcio:  Exercici 1: Animals 

class Animal:
    def parlar(self):
        pass
    
class Gos(Animal):
    def parlar(self):
        print("Bup bup!")
        
class Gat(Animal):
    def parlar(self):
        print("Miau!")
        
gos = Gos()
gat = Gat()

gos.parlar()  
gat.parlar()  
    