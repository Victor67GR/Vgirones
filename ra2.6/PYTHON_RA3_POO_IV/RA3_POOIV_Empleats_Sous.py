#Víctor Gironés Roca
#ASIX (Administració de Sistemes Informàtics en Xarxa)
#11/02/2026
#Descipcio: Polimorfisme Exercici 3: Empleats i sous 

class Empleat:
    def calcular_sou(self):
        pass
    
class Fixe(Empleat):
    def __init__(self, salari_base):
        self.salari_base = salari_base
        
    def calcular_sou(self):
        return self.salari_base
    
class Autonom(Empleat):
    def __init__(self, hores, tarifa):
        self.hores = hores
        self.tarifa = tarifa
        
    def calcular_sou(self):
        return self.hores * self.tarifa
    
def mostrar_sous(llista_empleats):
    for empleat in llista_empleats:
        print(f"Sou de {empleat.__class__.__name__}: {empleat.calcular_sou()}")
empleats = [Fixe(2000), Autonom(160, 15)]
mostrar_sous(empleats)
