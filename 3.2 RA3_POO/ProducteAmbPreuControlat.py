# Nom i cognoms: Victor Girones Estudiant de Asix
# Data: 21/01/2026
# Descripció: Plantilla per scripts en bash
# 6. Producte amb preu controlat Classe Producte amb atributs: nom (públic) __preu (privat) Mètodes per obtenir i modificar el preu (només si > 0)

class Producte:

    def __init__(self, nom, preu):
        self.nom = nom
        self.__preu = preu

    @property
    def preu(self):
        return self.__preu

    @preu.setter
    def preu(self, preu):
        if preu > 0:
            self.__preu = preu
        else:
            print("El preu ha de ser major que 0.")

producte1 = Producte("Llibre", 15.0)
print("Nom del producte:", producte1.nom)
print("Preu del producte:", producte1.preu)

producte1.preu = 20.0
print("Nou preu del producte:", producte1.preu) 
