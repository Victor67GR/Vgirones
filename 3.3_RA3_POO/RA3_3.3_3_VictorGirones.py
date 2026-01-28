# Nom i cognoms: Victor Girones Estudiant de Asix
# Data: 28/01/2026
# Descripció: Plantilla per scripts en bash

class CarretCompra:
    def __init__(self, total, descompte):
        self.total = total
        self.descomte = descompte

    def calcular_total_amb_descompte(self):
        return self.descomte.aplicar(self.total)

class Descompte20:
    def aplicar(self, total):
        return total * 0.8
    