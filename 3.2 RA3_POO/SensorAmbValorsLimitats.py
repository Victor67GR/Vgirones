# Nom i cognoms: Victor Girones Estudiant de Asix
# Data: 21/01/2026
# Descripció: Plantilla per scripts en bash

class Sensor:

    def __init__(self, valor):
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        if 0 <= valor <= 100:
            self.__valor = valor
        else:
            print("El valor ha d'estar entre 0 i 100.")

sensor1 = Sensor(50)
print("El valor actual del sensor és:", sensor1.valor)  
sensor1.valor = 75
print("El nou valor del sensor és:", sensor1.valor)
