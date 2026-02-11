#Víctor Gironés Roca
#ASIX (Administració de Sistemes Informàtics en Xarxa)
#11/02/2026
#Descipcio: Exercici 5: Biblioteca

class Llibre:
    def __init__(self, titol, autor):
        self.titol = titol
        self.autor = autor
        
    def mostrar_info(self):
        print(f"Títol: {self.titol}, Autor: {self.autor}")

class LlibrePaper(Llibre):
    def __init__(self, titol, autor, n_pagines):
        super().__init__(titol, autor)
        self.n_pagines = n_pagines
        
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de pàgines: {self.n_pagines}")
        

class LlibreDigital(Llibre):
    def __init__(self, titol, autor, format):
        super().__init__(titol, autor)
        self.format = format
        
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Format: {self.format}")
        
llibre_paper = LlibrePaper("El Quijote", "Miguel de Cervantes", 863)
llibre_digital = LlibreDigital("1984", "George Orwell", "PDF")
llibre_paper.mostrar_info()
print()
llibre_digital.mostrar_info()
