# # Nom i cognoms: Victor Girones Estudiant de Asix
# Data: 21/01/2026
# Descripció: Plantilla per scripts en bash

class Rellotge:

    def __init__(self, hores):
        self.__hores = hores

    @property
    def hores(self):
        return self.__hores

    @hores.setter
    def hores(self, hores):
        if 0 <= hores <= 23:
            self.__hores = hores
        else:
            print("Les hores han d'estar entre 0 i 23.")

    def mostrar_hora(self):
        return f"{self.__hores:02d}:00"

rellotge1 = Rellotge(10)
print("Hora actual:", rellotge1.mostrar_hora())

rellotge1.hores = 15
print("Nova hora:", rellotge1.mostrar_hora())
