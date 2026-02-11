#Víctor Gironés Roca
#ASIX (Administració de Sistemes Informàtics en Xarxa)
#11/02/2026
#Descipcio: Exercici 3: Persones i treballadors 

class Persona:
    def __init__(self, nom, edat):
        self.nom = nom
        self.edat = edat
        
    def saludar(self):
        print(f"Hola, sóc {self.nom}.")
    
class Treballador(Persona):
    def __init__(self, nom, edat, feina):
        super().__init__(nom, edat)
        self.feina = feina
        
    def mostrar_feina(self):
        print(f"Treballo com a {self.feina}.")
    
treballador = Treballador("Víctor", 18, "programador")
treballador.saludar()
treballador.mostrar_feina()