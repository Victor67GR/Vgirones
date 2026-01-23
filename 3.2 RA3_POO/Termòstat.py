# Nom i cognoms: Victor Girones Estudiant de Asix
# Data: 21/01/2026
# Descripció: Plantilla per scripts en bash

class termostat:

    def __init__(self,temperatura):
        self.__temperatura = temperatura

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, temperatura):
        if temperatura >= 10 and temperatura <= 30:
            self.__temperatura = temperatura
        else:
            print("La temperatura ha d'estar entre 10 i 30 °C")

termostat1 = termostat(20)
print("La temperatura actual és: ", termostat1.temperatura)

termostat1.temperatura = 25
print("La nova temperatura és: ", termostat1.temperatura)

