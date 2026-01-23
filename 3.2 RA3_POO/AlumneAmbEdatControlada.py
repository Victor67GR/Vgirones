# Nom i cognoms: Victor Girones Estudiant de Asix
# Data: 21/01/2026
# Descripció: Plantilla per scripts en bash

class Alumne:

    def __init__(self, edat):
        self.__edat = edat

    @property
    def edat(self):
        return self.__edat

    @edat.setter
    def edat(self, edat):
        if edat >= 0:
            self.__edat = edat
        else:
            print("L'edat no pot ser negativa.")

alumne1 = Alumne(20)
print("Edat actual de l'alumne:", alumne1.edat)

alumne1.edat = 22
print("Nova edat de l'alumne:", alumne1.edat)
