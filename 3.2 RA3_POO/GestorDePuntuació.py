# Nom i cognoms: Victor Girones Estudiant de Asix
# Data: 21/01/2026
# Descripció: Plantilla per scripts en bash

class Joc:

    def __init__(self):
        self.__puntuacio = 0

    @property
    def puntuacio(self):
        return self.__puntuacio

    def sumar_punts(self, punts):
        if punts > 0:
            self.__puntuacio += punts
        else:
            print("Els punts a sumar han de ser positius.")

    def reiniciar_puntuacio(self):
        self.__puntuacio = 0

joc1 = Joc()
print("Puntuació inicial del joc:", joc1.puntuacio)

joc1.sumar_punts(10)
print("Puntuació després de sumar punts:", joc1.puntuacio)

joc1.reiniciar_puntuacio()
print("Puntuació després de reiniciar:", joc1.puntuacio)
