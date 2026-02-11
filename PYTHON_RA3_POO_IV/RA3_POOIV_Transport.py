#Víctor Gironés Roca
#ASIX (Administració de Sistemes Informàtics en Xarxa)
#11/02/2026
#Descipcio: Polimorfisme Exercici 5: Transport 

class Vehicle:
    def moure(self):
        pass
    
class Cotxe(Vehicle):
    def moure(self):
        print("El cotxe està conduint per la carretera.")
        
class Bicicleta(Vehicle):
    def moure(self):
        print("La bicicleta està pedalant per el parc.")

class Barca(Vehicle):
    def moure(self):
        print("La barca està navegant pel riu.")
        
def simular_moviment(vehicles):
    for vehicle in vehicles:
        vehicle.moure()
        
vehicles = [Cotxe(), Bicicleta(), Barca()]
simular_moviment(vehicles)