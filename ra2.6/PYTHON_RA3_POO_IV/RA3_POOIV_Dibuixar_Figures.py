#Víctor Gironés Roca
#ASIX (Administració de Sistemes Informàtics en Xarxa)
#11/02/2026
#Descipcio: Polimorfisme Exercici 2: Dibuixar figures 
 
class Figura:
    def dibuixar(self):
        print("Dibuixant una figura genèrica.")
        
class Cercle(Figura):
    def dibuixar(self):
        print("Dibuixant un cercle.")
        
class Quadrat(Figura):
    def dibuixar(self):
        print("Dibuixant un quadrat.")
        
class Triangle(Figura):
    def dibuixar(self):
        print("Dibuixant un triangle.")
        
figures = [Cercle(), Quadrat(), Triangle()]
for figura in figures:
    figura.dibuixar() 

